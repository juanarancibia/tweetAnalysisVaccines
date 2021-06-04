import io
import pandas as pd
import sentimentAnalysis

# df = pd.read_json('./Datos/vacunasXFrase.json')
# df.drop_duplicates(subset='id', keep="last")
# dfNoRTS = df[df['retweet'] == False]
# tweetsDict = trolls.detectTrollTweets(dfNoRTS['tweet'])

# df = pd.read_json('./Datos/vacunasXFrase.json')

# popularDf = df[(df['likes_count'] > 30000)]
# print(len(popularDf['tweet']))
# for tweet in popularDf['tweet']:
#     print(tweet)

# df = pd.read_csv('./Datos/vacunasXFraseLimpiasConStopwords.csv')

# df['sentiment_analysis'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_pypi((x.replace('[', '').replace(']', '').replace("'", '').replace(',', ''))))
# print('Ready')

# df.to_csv('./Datos/vacunasXFraseSentimientosConStopwordsV2.csv')




