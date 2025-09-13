from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Crear sesión Spark
spark = SparkSession.builder.appName("SegmentacionClientes").getOrCreate()

# Cargar dataset
df = spark.read.csv("clientes_segmentacion.csv", header=True, inferSchema=True)

# Ensamblar features
assembler = VectorAssembler(
    inputCols=["edad", "ingresos", "frecuencia_compra"],
    outputCol="features"
)
df_features = assembler.transform(df)

# Aplicar K-Means
kmeans = KMeans().setK(4).setSeed(1).setFeaturesCol("features")
model = kmeans.fit(df_features)

# Predicciones
predictions = model.transform(df_features)
predictions.show()

# Evaluación con Silhouette Score
evaluator = ClusteringEvaluator(featuresCol="features", predictionCol="prediction", metricName="silhouette")
silhouette = evaluator.evaluate(predictions)
print(f"Silhouette Score: {silhouette}")


# Convertir el DataFrame de Spark a Pandas para graficar
pdf = predictions.select("edad", "ingresos", "frecuencia_compra", "prediction").toPandas()

# Crear gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Colores para cada clúster
colors = ['red', 'blue', 'green', 'orange']

for cluster in sorted(pdf['prediction'].unique()):
    subset = pdf[pdf['prediction'] == cluster]
    ax.scatter(subset['edad'], subset['ingresos'], subset['frecuencia_compra'],
               c=colors[cluster], label=f"Clúster {cluster}", s=60)

# Etiquetas
ax.set_xlabel('Edad')
ax.set_ylabel('Ingresos')
ax.set_zlabel('Frecuencia de Compra')
ax.set_title('Segmentación de Clientes por K-Means')
ax.legend()

plt.show()
