
@echo off

REM Iniciar Kafka y Zookeeper con docker-compose
echo Iniciando Kafka y Zookeeper...
docker-compose up -d

REM Esperar unos segundos para que los servicios arranquen completamente
timeout /t 5

REM Verificar si el tópico 'mi-topico' existe
echo Verificando existencia del tópico 'mi-topico'...
docker exec kafka kafka-topics --bootstrap-server localhost:9092 --list | findstr "mi-topico"
IF %ERRORLEVEL% NEQ 0 (
    echo Tópico 'mi-topico' no existe. Creando...
    docker exec kafka kafka-topics --bootstrap-server localhost:9092 --create --topic mi-topico --partitions 1 --replication-factor 1
) ELSE (
    echo Tópico 'mi-topico' ya existe.
)

pause
