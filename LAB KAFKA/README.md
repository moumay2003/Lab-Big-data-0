# Kafka Lab - Producer & Consumer Application

## Structure du Projet
```
LAB KAFKA/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── edu/
                └── ensias/
                    └── kafka/
                        ├── EventProducer.java
                        └── EventConsumer.java
```

## Étapes de Construction et Exécution

### 1. Compiler le Projet
Dans le répertoire `LAB KAFKA`, exécutez:
```bash
mvn clean package
```

Cela va créer deux JARs:
- `target/kafka-producer-app-jar-with-dependencies.jar`
- `target/kafka-consumer-app-jar-with-dependencies.jar`

### 2. Copier les JARs dans le Container Docker

#### Option A: Utiliser un volume partagé
```powershell
# Copier vers le dossier partagé (si configuré dans docker-compose)
Copy-Item "target\kafka-producer-app-jar-with-dependencies.jar" -Destination ".\shared_volume\kafka\"
Copy-Item "target\kafka-consumer-app-jar-with-dependencies.jar" -Destination ".\shared_volume\kafka\"
```

#### Option B: Utiliser docker cp
```powershell
docker cp target\kafka-producer-app-jar-with-dependencies.jar hadoop-master:/root/
docker cp target\kafka-consumer-app-jar-with-dependencies.jar hadoop-master:/root/
```

### 3. Exécuter le Producer
Dans le container hadoop-master:
```bash
docker exec -it hadoop-master bash

# Créer le topic si nécessaire
kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Hello-Kafka

# Lancer le producer
java -jar /root/kafka-producer-app-jar-with-dependencies.jar Hello-Kafka
```

**Résultat attendu**: `Message envoye avec succes`

### 4. Vérifier les Messages

#### Option 1: Utiliser le Consumer Kafka en ligne de commande
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Hello-Kafka --from-beginning
```

#### Option 2: Utiliser votre EventConsumer Java
```bash
java -jar /root/kafka-consumer-app-jar-with-dependencies.jar Hello-Kafka
```

**Résultat attendu**: Affichage de 10 messages (0-9) avec leurs offsets, clés et valeurs

### 5. Exemple de Sortie

**Producer:**
```
Message envoye avec succes
```

**Consumer:**
```
Souscris au topic Hello-Kafka
offset = 0, key = 0, value = 0
offset = 1, key = 1, value = 1
offset = 2, key = 2, value = 2
offset = 3, key = 3, value = 3
offset = 4, key = 4, value = 4
offset = 5, key = 5, value = 5
offset = 6, key = 6, value = 6
offset = 7, key = 7, value = 7
offset = 8, key = 8, value = 8
offset = 9, key = 9, value = 9
```

## Configuration

### EventProducer
- **bootstrap.servers**: localhost:9092
- **acks**: all (garantit que tous les réplicas ont reçu le message)
- **retries**: 0 (nombre de tentatives en cas d'échec)
- **batch.size**: 16384 bytes
- **buffer.memory**: 33554432 bytes (32 MB)

### EventConsumer
- **bootstrap.servers**: localhost:9092
- **group.id**: test
- **enable.auto.commit**: true
- **auto.commit.interval.ms**: 1000
- **session.timeout.ms**: 30000

## Notes
- Le Producer envoie 10 messages (clé et valeur de 0 à 9)
- Le Consumer lit continuellement les messages jusqu'à interruption (Ctrl+C)
- ProducerRecord est un couple <clé, valeur> envoyé au cluster Kafka
