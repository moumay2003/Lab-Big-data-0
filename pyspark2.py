import pyspark2
from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("MyApp").getOrCreate()
sc = spark.sparkContext  
data=sc.textFile("hdfs://hadoop-master:9000/user/root/input/alice.txt")
words=data.flatMap(lambda line: line.split(" "))
wordCounts=words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
wordCounts.saveAsTextFile("hdfs://hadoop-master:9000/user/root/output/wordcount")
spa