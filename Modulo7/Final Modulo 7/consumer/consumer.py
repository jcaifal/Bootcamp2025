from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'mi-topico',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='mi-grupo'
)

print("Esperando mensajes...")
for message in consumer:
    print(f"Mensaje recibido: {message.value.decode('utf-8')}")
