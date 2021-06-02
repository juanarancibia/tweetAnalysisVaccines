from numpy import nan
from sentiment_analysis_spanish import sentiment_analysis

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

def analize_sentiment_pypi(tweet):
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
        
    return sentimiento, sentimientoCualitativo