from pyspark.sql import SparkSession
from operator import add
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk 
nltk.download('vader_lexicon')
import re

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

def Simons_task():
    data = spark.read.json("sample_data.json")
    # Drop all columns except body and score
    data2 = data.select(data["body"], data["score"])
    
    # make into rdd
    data2_rdd = data2.rdd
    # Split the body into words and remove all non-alphanumeric characters
    data2_rdd_split = data2_rdd.map(lambda x: ([re.sub(r'\W+', '', s).lower() for s in x[0].split()], x[1]))
    # Remove words longer than 20 characters
    data2_rdd_split = data2_rdd_split.map(lambda x: ([s for s in x[0] if len(s) <= 20], x[1]))
    # Separate the words into tuples with the score
    data2_rdd_split_score = data2_rdd_split.flatMap(lambda x: [(s, x[1]) for s in x[0]])
    # Show the data

        # Group the words by word and sum the score
    data2_scored_words = data2_rdd_split_score.reduceByKey(lambda x, y: x + y)
    # Sort the data by score
    data2_scored_words = data2_scored_words.sortBy(lambda x: x[1], ascending=False)
    # Show most "negative" words
    #data2_scored_words = data2_scored_words.sortBy(lambda x: x[1], ascending=True)

    # Convert score to "Positive" or "Negative"
    data2_score_based = data2_scored_words.map(lambda x: (x[0], "Positive" if x[1] > 0 else "Negative"))
    # Convert to dataframe
    data2_score_based_df = data2_score_based.toDF(["Word", "Score"])
    # Save the data to a file
    #data2_score_based_df.write.csv("data2_score_based.csv")

def task_2():
    data = spark.read.json("sample_data.json")
    data1 = data.groupBy(data["subreddit"]).count()
    data2 = data1.orderBy("count", ascending=False)
    return data.take(10)


