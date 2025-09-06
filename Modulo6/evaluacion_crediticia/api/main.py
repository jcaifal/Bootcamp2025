# archivo: api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API Evaluación Crediticia")

# Cargar modelo
modelo = joblib.load("modelo_crediticio.pkl")

# Esquema de entrada
class Cliente(BaseModel):
    edad: int
    ingresos: float
    historial_crediticio: str
    deuda: float
    empleado: str

@app.post("/predict")
def predecir(cliente: Cliente):
    df = pd.DataFrame([cliente.dict()])
    prediccion = modelo.predict(df)[0]
    probabilidad = modelo.predict_proba(df)[0][1]
    return {
        "apto_credito": bool(prediccion),
        "probabilidad": round(probabilidad, 2)
    }

print("DEBUG: __name__ is", __name__)
print("DEBUG: app is", 'app' in globals())

@app.get("/")
def root():
    return {"mensaje": "API Evaluación Crediticia funcionando correctamente"}
