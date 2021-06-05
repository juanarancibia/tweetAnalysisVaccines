import pandas as pd
import trolls

df = pd.read_json('./Datos/vacunasXFrase.json')
df.drop_duplicates(subset='id', keep="last")
dfNoRTS = df[df['retweet'] == False]
tweetsDict = trolls.detectTrollTweets(dfNoRTS['tweet'])
troll_tweet, amount = zip(*tweetsDict.items())
new_df = pd.DataFrame()
new_df['Tweet'] = troll_tweet
new_df['Amount'] = amount

new_df.to_csv('./Data/trollsTweets.csv')

# df = pd.read_json('./Datos/vacunasXFrase.json')

# popularDf = df[(df['likes_count'] > 30000)]
# print(len(popularDf['tweet']))
# for tweet in popularDf['tweet']:
#     print(tweet)

# df = pd.read_csv('./Datos/vacunasXFraseLimpiasConStopwords.csv')

# df['sentiment_analysis'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_discretized_3rd(str(x)))
# print('Ready')

# df.to_csv('./Datos/vacunasXFraseSentimientosConStopwordsV3.csv')




