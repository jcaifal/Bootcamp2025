from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Crear sesión de Spark
spark = SparkSession.builder.appName("ModeloCompraClientes").getOrCreate()

# Cargar datos
df = spark.read.csv("clientes.csv", header=True, inferSchema=True)

# Limpiar datos nulos
df = df.dropna()

# Indexar variable categórica
indexer = StringIndexer(inputCol="genero", outputCol="genero_index")
df = indexer.fit(df).transform(df)

# Vectorizar características
assembler = VectorAssembler(
    inputCols=["edad", "ingresos", "genero_index", "historial_compras"],
    outputCol="features"
)
df = assembler.transform(df).select("features", col("compra").alias("label"))

# Dividir datos
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Modelo Random Forest
rf = RandomForestClassifier()

# Validación cruzada y ajuste de hiperparámetros
paramGrid = ParamGridBuilder()     .addGrid(rf.maxDepth, [5, 10])     .addGrid(rf.numTrees, [50, 100])     .build()

evaluator = BinaryClassificationEvaluator()

cv = CrossValidator(estimator=rf,
                    estimatorParamMaps=paramGrid,
                    evaluator=evaluator,
                    numFolds=5)

cv_model = cv.fit(train_data)

# Evaluación
predictions = cv_model.transform(test_data)
auc = evaluator.evaluate(predictions)
accuracy = predictions.filter(predictions.label == predictions.prediction).count() / predictions.count()

print(f"AUC: {auc:.4f}")
print(f"Precisión: {accuracy:.4f}")
