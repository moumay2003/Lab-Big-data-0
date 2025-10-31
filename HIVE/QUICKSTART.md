# 🚀 Guide de Démarrage Rapide - Hive Lab

## Option 1 : Déploiement Automatique (Recommandé)

### Étape 1 : Exécuter le script de déploiement
```powershell
cd "c:\Users\mouad\OneDrive - um5.ac.ma\Desktop\Lab Big data 0\HIVE"
.\deploy.ps1
```

Ce script va :
- ✅ Créer les répertoires nécessaires
- ✅ Copier les données et scripts
- ✅ Démarrer Docker Compose
- ✅ Vérifier que HiveServer2 est opérationnel

### Étape 2 : Exécuter les scripts Hive
```bash
# Accéder au conteneur
docker exec -it hiveserver2-standalone bash

# 1. Créer la base de données et les tables
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Creation.hql

# 2. Charger les données
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Loading.hql

# 3. Exécuter les requêtes
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Queries.hql
```

---

## Option 2 : Déploiement Manuel

### Étape 1 : Préparer les dossiers
```powershell
# Créer les dossiers
New-Item -ItemType Directory -Force -Path "C:\Users\mouad\OneDrive - um5.ac.ma\Documents\hadoop_project\hive\data"
New-Item -ItemType Directory -Force -Path "C:\Users\mouad\OneDrive - um5.ac.ma\Documents\hadoop_project\hive\scripts"

# Copier les fichiers
Copy-Item -Path "HIVE\data\*" -Destination "C:\Users\mouad\OneDrive - um5.ac.ma\Documents\hadoop_project\hive\data\"
Copy-Item -Path "HIVE\scripts\*" -Destination "C:\Users\mouad\OneDrive - um5.ac.ma\Documents\hadoop_project\hive\scripts\"
```

### Étape 2 : Démarrer Docker Compose
```powershell
cd "c:\Users\mouad\OneDrive - um5.ac.ma\Desktop\Lab Big data 0"
docker-compose up -d
```

### Étape 3 : Attendre le démarrage (30 secondes)
```powershell
Start-Sleep -Seconds 30
```

### Étape 4 : Vérifier
```powershell
docker ps | findstr hive
```

### Étape 5 : Exécuter les scripts
```bash
docker exec -it hiveserver2-standalone bash

# Création
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Creation.hql

# Chargement
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Loading.hql

# Requêtes
beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Queries.hql
```

---

## 🌐 Accès Web

- **HiveServer2 Web UI**: http://localhost:10002
- **Hadoop NameNode UI**: http://localhost:9870
- **Hadoop ResourceManager**: http://localhost:8088

---

## 📊 Vérification Rapide

### Dans Beeline
```sql
-- Se connecter
docker exec -it hiveserver2-standalone beeline -u jdbc:hive2://localhost:10000 scott tiger

-- Vérifier
SHOW DATABASES;
USE hotel_booking;
SHOW TABLES;
SELECT COUNT(*) FROM clients;
SELECT COUNT(*) FROM reservations;

-- Quitter
!quit
```

---

## 🛑 Arrêter les Services

```powershell
docker-compose down
```

---

## 🔄 Redémarrer Proprement

```powershell
# Arrêter
docker-compose down

# Redémarrer
docker-compose up -d

# Attendre
Start-Sleep -Seconds 30
```

---

## 📝 Commandes Utiles

### Vérifier les logs
```powershell
docker logs hiveserver2-standalone
docker logs hadoop-master
```

### Nettoyer tout
```bash
# Dans le conteneur Hive
docker exec -it hiveserver2-standalone beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Cleanup.hql
```

### Réinitialiser les données
```bash
# Supprimer et recréer
docker exec -it hiveserver2-standalone bash -c "
  beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Cleanup.hql && \
  beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Creation.hql && \
  beeline -u jdbc:hive2://localhost:10000 scott tiger -f /shared_volume/hive/scripts/Loading.hql
"
```

---

## ✅ Checklist

- [ ] Script deploy.ps1 exécuté avec succès
- [ ] Docker containers en cours d'exécution
- [ ] Accès à http://localhost:10002 fonctionnel
- [ ] Base de données hotel_booking créée
- [ ] Données chargées (10 clients, 10 hôtels, 15 réservations)
- [ ] Requêtes testées et fonctionnelles

---

**Bon Lab! 🎓**
