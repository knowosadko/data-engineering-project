from pyspark.sql import SparkSession
from operator import add
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk 
nltk.download('vader_lexicon')

spark = SparkSession.builder\
        .master("spark://192.168.2.186:7077") \
        .appName("Group14_Application")\
        .config("spark.cores.max", 4)\
        .getOrCreate()
        
def task_1():
    ranges = [i/10 for i in range(-10,11,1)]
    
    def assign_num(value):
        i = 0
        while ranges[i] < value:
            i+=1
        return i
    
    sia = SentimentIntensityAnalyzer()
    data = spark.read.json("sample_data.json")
    body = data.select("id","body","score")
    rdd2=body.rdd.map(lambda x: (x["id"],x["body"],x["score"] ,sia.polarity_scores(x['body'])["compound"]))
    results = rdd2.toDF(["id","body","score","sentiment"])
    rdd3 = results.rdd.map(lambda x: 
    (assign_num(x['sentiment']),1)).reduceByKey(add)
    return rdd3.take(20)

