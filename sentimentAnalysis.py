from numpy import nan
from sentiment_analysis_spanish import sentiment_analysis

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

def analize_sentiment_pypi(tweet):
    if tweet is nan:
        return "Error"

    sentimiento = sentiment.sentiment(tweet)
    if(sentimiento < 0.15):
        sentimiento = "Negativo"
    elif (sentimiento < 0.4):
        sentimiento = "Neutro"
    else:
        sentimiento = "Positivo"
    return sentimiento