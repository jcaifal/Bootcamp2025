from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Crear sesión Spark
spark = SparkSession.builder.appName("PipelineClasificacion").getOrCreate()

# Leer el CSV
df = spark.read.csv("dataset_clasificacion.csv", header=True, inferSchema=True)
df.printSchema()

# Indexar variables categóricas
indexers = [
    StringIndexer(inputCol="categoria1", outputCol="categoria1_indexed"),
    StringIndexer(inputCol="categoria2", outputCol="categoria2_indexed")
]

# Ensamblar features
assembler = VectorAssembler(
    inputCols=["categoria1_indexed", "categoria2_indexed", "numerica1", "numerica2"],
    outputCol="features"
)

# Modelo de regresión logística
lr = LogisticRegression(featuresCol="features", labelCol="label")

# Crear pipeline
pipeline = Pipeline(stages=indexers + [assembler, lr])

# Dividir datos
train, test = df.randomSplit([0.7, 0.3], seed=42)

# Entrenar modelo
model = pipeline.fit(train)

# Evaluar modelo
predictions = model.transform(test)
evaluator = BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)

print(f"AUC: {auc}")
