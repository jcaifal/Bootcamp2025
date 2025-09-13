
# Segmentación de Clientes con K-Means en MLlib

Este proyecto implementa un pipeline de clustering utilizando el algoritmo K-Means de MLlib en PySpark para segmentar clientes según edad, ingresos y frecuencia de compra.

## 📁 Estructura del Proyecto

```
segmentacion_clientes/
├── clientes_segmentacion.csv         # Dataset con 20 ejemplos
├── main.py                           # Script principal con el pipeline MLlib
├── README.md                         # Documentación del proyecto
└── requirements.txt                  # Dependencias del entorno
```

## 🚀 Ejecución del Proyecto

1. Clona o descarga este repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el script principal:
   ```bash
   python main.py
   ```

## 🧪 Dataset
El archivo `clientes_segmentacion.csv` contiene 20 registros con las siguientes columnas:
- `edad`
- `ingresos`
- `frecuencia_compra`

## 🧠 Interpretación de Resultados
El script aplica K-Means con 4 clústeres y evalúa la cohesión del agrupamiento usando Silhouette Score. Un valor cercano a 1 indica buena separación entre clústeres.

## 🛠️ Requisitos
- Python 3.8+
- PySpark

