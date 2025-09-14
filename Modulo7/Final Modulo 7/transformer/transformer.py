from kafka import KafkaProducer
import time

# Leer el archivo eventos.csv
with open("data/eventos.csv", "r", encoding="utf-8") as f:
    eventos = f.readlines()

# Crear el productor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')
)

# Enviar cada línea como mensaje al tópico 'mi-topico'
for i, evento in enumerate(eventos):
    evento = evento.strip()
    if evento:
        producer.send('mi-topico', value=evento)
        print(f"[{i+1}/{len(eventos)}] Mensaje enviado: {evento}")
        time.sleep(0.1)  # Puedes ajustar o eliminar esta pausa

producer.flush()
producer.close()
print("Todos los mensajes han sido enviados.")
