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
```powershell
cd "c:\Users\mouad\OneDrive - um5.ac.ma\Desktop\Lab Big data 0\LAB KAFKA"
mvn clean package
```

Cela va créer deux JARs dans le dossier `target/`:
- `kafka-producer-app-jar-with-dependencies.jar`
- `kafka-consumer-app-jar-with-dependencies.jar`

### 2. Copier les JARs dans le Container Docker
```powershell
docker cp target\kafka-producer-app-jar-with-dependencies.jar hadoop-master:/root/
docker cp target\kafka-consumer-app-jar-with-dependencies.jar hadoop-master:/root/
```

### 3. Exécuter le Producer
```bash
docker exec -it hadoop-master bash

# Créer le topic si nécessaire
kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic Hello-Kafka

# Lancer le producer
java -jar /root/kafka-producer-app-jar-with-dependencies.jar Hello-Kafka
```

**Résultat attendu**: `Message envoye avec succes`

### 4. Vérifier les Messages avec le Consumer
```bash
# Dans un autre terminal
docker exec -it hadoop-master bash
java -jar /root/kafka-consumer-app-jar-with-dependencies.jar Hello-Kafka
```

**Ou utiliser le consumer en ligne de commande:**
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Hello-Kafka --from-beginning
```

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
...
offset = 9, key = 9, value = 9
```

## Configuration

### EventProducer
- Envoie 10 messages (clé et valeur de 0 à 9)
- **bootstrap.servers**: localhost:9092
- **acks**: all (garantit que tous les réplicas ont reçu le message)
- **batch.size**: 16384 bytes
- **buffer.memory**: 33554432 bytes (32 MB)

### EventConsumer
- Lit continuellement les messages
- **bootstrap.servers**: localhost:9092
- **group.id**: test
- **enable.auto.commit**: true
