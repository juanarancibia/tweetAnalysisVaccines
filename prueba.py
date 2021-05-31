import re
import string
from numpy import nan
import pandas as pd
from googletrans import Translator
from sentiment_analysis_spanish import sentiment_analysis
from textblob import TextBlob
import time

regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)

def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = regrex_pattern.sub(r'',tweet) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet =re.sub("\W", " ", tweet).lower() #Remove punctuation
    print(tweet) 
    return tweet

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

def analize_sentiment_pypi(tweet):
    if tweet is nan:
        return "Error"

    sentimiento = sentiment.sentiment(tweet)
    if(sentimiento < 0.3):
        sentimiento = "Negativo"
    elif (sentimiento < 0.6):
        sentimiento = "Neutro"
    else:
        sentimiento = "Positivo"
    print (sentimiento)
    return sentimiento

def traduce(tweet):
    text = TextBlob(tweet)
    translated = text.translate(to="en")
    print(translated)
    return translated

def analize_sentiment_textblob(tweet):
    text = TextBlob(tweet)
    sentiment = text.sentiment()
    print(sentiment)
    return sentiment


# df = pd.read_json('vacunasXFrase.json')

# df.drop_duplicates(subset='id', keep='first')

# df['tweet'] = df['tweet'].map(lambda x: cleaner(x))

# df.to_json("vacunasXFraseLimpias.json")
# df.to_csv("vacunasXFraseLimpias.csv")



df = pd.read_csv('./Datos/vacunasXFrasePypi.csv')

# df['sentiment_analysis_pypi'] = df['tweet'].map(lambda x: analize_sentiment_pypi(x))
# df["sentiment_analysis_textblob'] = df['tweet'].map(lambda x: analize_sentiment_textblob(x))

df['translated_tweet'] = df['tweet'].map(lambda x: traduce(x))

df.to_csv("./Datos/vacunasXFraseTraducida.csv")
df.to_json("./Datos/vacunasXFraseTraducida.json")

#df["sentiment_analysis_textblob"], df["polarity_analysis_textblob"] = df['translated_tweet'].map(lambda x: analize_sentiment_textblob(x))

# df.to_csv("vacunasXMarcaNoviembreTextBlob.csv")
