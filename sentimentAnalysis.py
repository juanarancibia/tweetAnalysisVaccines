from numpy import nan
from sentiment_analysis_spanish import sentiment_analysis

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

def analize_sentiment_value(tweet):
    if tweet is nan:
        return "Error"
    sentimiento = sentiment.sentiment(tweet)
    return sentimiento

def analize_sentiment_discretized_3rd(tweet):
    if tweet is nan:
        return "Error"
    sentimientoCualitativo = ""
    sentimiento = sentiment.sentiment(tweet)
    if(sentimiento < 0.05):
        sentimientoCualitativo = "Negativo"
    elif (sentimiento < 0.30):
        sentimientoCualitativo = "Neutro"
    else:
        sentimientoCualitativo = "Positivo"
    
    return sentimientoCualitativo

def analize_sentiment_discretized_2nd(tweet):
    if tweet is nan:
        return "Error"
    sentimientoCualitativo = ""
    sentimiento = sentiment.sentiment(tweet)
    if(sentimiento < 0.06):
        sentimientoCualitativo = "Negativo"
    elif (sentimiento < 0.40):
        sentimientoCualitativo = "Neutro"
    else:
        sentimientoCualitativo = "Positivo"
        
    return sentimientoCualitativo


def analize_sentiment_discretized_1st(tweet):
    if tweet is nan:
        return "Error"
    sentimientoCualitativo = ""
    sentimiento = sentiment.sentiment(tweet)
    if(sentimiento < 0.3):
        sentimientoCualitativo = "Negativo"
    elif (sentimiento < 0.6):
        sentimientoCualitativo = "Neutro"
    else:
        sentimientoCualitativo = "Positivo"
        
    return sentimientoCualitativo
    