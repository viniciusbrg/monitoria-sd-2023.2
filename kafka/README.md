

# Executando Kafka

Crie uma rede pro kafka `docker network create app-tier --driver bridge`

```bash
docker run --rm --name kafka-server --hostname kafka-server \
    --network app-tier \
    -p 9094:9094 \
    -e KAFKA_CFG_NODE_ID=0 \
    -e KAFKA_CFG_PROCESS_ROLES=controller,broker \
    -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093,EXTERNAL://:9094 \
    -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka-server:9092,EXTERNAL://localhost:9094 \
    -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,EXTERNAL:PLAINTEXT,PLAINTEXT:PLAINTEXT \
    -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka-server:9093 \
    -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER \
    bitnami/kafka:latest
    
    
```

Executando Redpanda Console pro Kafka

```
docker run --network app-tier -p 8080:8080 -e KAFKA_BROKERS=kafka-server:9092 docker.redpanda.com/redpandadata/console:latest
```

Crie um virtualenv e instale a lib do kafka

`pip install confluent-kafka`
