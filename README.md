# Mini-rapport – TP Apache Spark : WordCount

## 1. Objectif du TP

L’objectif de ce travail pratique est de se familiariser avec l’écosystème **Apache Spark** en environnement distribué, en manipulant des données stockées dans **HDFS**, et en implémentant l’algorithme classique **WordCount** en deux langages : **Scala** (via le Spark Shell) et **Python** (via spark-submit).

## 2. Environnement de travail

* **Plateforme** : Cluster Hadoop exécuté dans des conteneurs Docker
* **Nœud principal** : `hadoop-master`
* **Framework Big Data** : Apache Spark
* **Système de fichiers distribué** : HDFS
* **Langages utilisés** : Scala et Python
* **Données d’entrée** : Fichier texte `alice.txt` stocké dans HDFS

## 3. Implémentation du WordCount en Scala

L’exécution Scala a été réalisée directement sur le nœud `hadoop-master` à l’aide du **Spark Shell**.

### Étapes principales :

1. Chargement du fichier texte depuis HDFS :

```scala
val data = sc.textFile("hdfs://hadoop-master:9000/user/root/input/alice.txt")
```

2. Transformation des données (split, map et reduce) afin de compter les occurrences de chaque mot :

```scala
val count = data
  .flatMap(line => line.split(" "))
  .map(word => (word, 1))
  .reduceByKey(_ + _)
```

3. Sauvegarde du résultat final dans HDFS :

```scala
count.saveAsTextFile("hdfs://hadoop-master:9000/user/root/output/respark1")
```

Cette exécution a permis de générer un répertoire de sortie dans HDFS contenant les résultats du comptage des mots.

## 4. Implémentation du WordCount en Python

Le même algorithme a été implémenté en **PySpark**, puis exécuté à l’aide de la commande **spark-submit**.

### Caractéristiques :

* Le code Python reproduit exactement la même logique que la version Scala.
* L’exécution via `spark-submit` permet de lancer une application Spark complète de manière autonome.
* Les résultats sont également stockés dans HDFS, dans un répertoire dédié (`output/wordcount`).

## 5. Résultats obtenus

Après l’exécution des deux versions (Scala et Python), la commande suivante permet de vérifier les répertoires de sortie :

```bash
hdfs dfs -ls /output
```

Deux dossiers sont présents :

* `output/respark1` : résultat du WordCount en Scala
* `output/wordcount` : résultat du WordCount en Python

Cela confirme le bon fonctionnement des deux implémentations et la persistance correcte des résultats dans HDFS.

## 6. Conclusion

Ce TP a permis :

* De comprendre le fonctionnement de Spark en mode distribué
* De manipuler HDFS pour la lecture et l’écriture de données
* De comparer l’exécution d’un même algorithme Spark en **Scala** et en **Python**
* D’utiliser deux modes d’exécution : **Spark Shell** et **spark-submit**

Ce travail constitue une base solide pour aborder des traitements Big Data plus complexes avec Apache Spark.
