import re
from nltk.corpus import stopwords

regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)

# stopwords = re.compile(r'(' + '|'.join(stopwords.words('spanish'))+r')')
# print(stopwords)
stopwords = stopwords.words('spanish')
stopwords.extend(["vacuna", "rusa", "china",
    'sputnik', 'sptunikv', 'rusia', 'q', 'xq', 'ahora', 'sinovac', 'sinopharm', 'aunque',
    'v', 'si', 'x'])

def clean(tweet):    
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remover signo @
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remover http links
    tweet = " ".join(tweet.split()) #Remover espacios multiples
    tweet = regrex_pattern.sub(r'',tweet) #Remover Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remover hashtag 
    tweet =re.sub("\W", " ", tweet).lower() #Remover puntuacion  
    
    tweet = tweet.lower().split()
    # clean_tweet = []
    # for item in tweet:  #Remover stopwords
    #     if item not in stopwords:
    #         clean_tweet.append(item)
    # clean_tweet = ' '.join(clean_tweet)         

    return tweet