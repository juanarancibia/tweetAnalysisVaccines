import pandas as pd

df = pd.read_json('./Datos/vacunasXFrase.json')

df['popularity'] = (df['likes_count'] + df['retweets_count'] + df['replies_count']) /3

popularDf = df.sort_values(by=['popularity'], ascending=False).head(1000)
#notLikedTweets = df.sort_values(by=['sentiment_value']).head(1000)

popularDf.drop(popularDf.columns.difference(['username', 'tweet', 'popularity', 'likes_count', 'retweets_count', 'replies_count', 'sentiment_analysis', 'date', 'link']),1,inplace=True)
#notLikedTweets.drop(notLikedTweets.columns.difference(['username', 'tweet', 'sentiment_value', 'sentiment_analysis', 'likes_count']),1,inplace=True)

popularDf.to_csv('./Data/popularTweets.csv')
#notLikedTweets.to_csv('./Data/mostNegativeTweets.csv')