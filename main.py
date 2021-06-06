import pandas as pd
from pandas.io.stata import PossiblePrecisionLoss
import trolls
import sentimentAnalysis

# df = pd.read_json('./Datos/vacunasXFrase.json')
# df.drop_duplicates(subset='id', keep="last")
# dfNoRTS = df[df['retweet'] == False]
# tweetsDict = trolls.detectTrollTweets(dfNoRTS['tweet'])
# troll_tweet, amount = zip(*tweetsDict.items())
# new_df = pd.DataFrame()
# new_df['Tweet'] = troll_tweet
# new_df['Amount'] = amount

# print(new_df['Amount'].sum())

df = pd.read_csv('./Datos/vacunasXFraseSentimientosConStopwordsV4.csv')

popularDf = df.sort_values(by=['likes_count'], ascending=False).head(1000)
notLikedTweets = df.sort_values(by=['sentiment_value']).head(1000)

popularDf.drop(popularDf.columns.difference(['username', 'tweet', 'likes_count', 'sentiment_analysis']),1,inplace=True)
notLikedTweets.drop(notLikedTweets.columns.difference(['username', 'tweet', 'sentiment_value', 'sentiment_analysis', 'likes_count']),1,inplace=True)

popularDf.to_csv('./Data/popularTweets.csv')
notLikedTweets.to_csv('./Data/mostNegativeTweets.csv')

# df = pd.read_csv('./Datos/vacunasXFraseLimpiasConStopwords.csv')

# df['sentiment_analysis'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_discretized_3rd(str(x)))
# df['sentiment_value'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_value(str(x)))
# print('Ready')

# df.to_csv('./Datos/vacunasXFraseSentimientosConStopwordsV4.csv')




