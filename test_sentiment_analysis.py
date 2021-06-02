import pandas as pd
import sentimentAnalysis

df = pd.read_csv('./Data/testSentiment.csv')
# df['index'] = df['Unnamed: 0']
# df.drop(df.columns.difference(['index','tweet']),1,inplace=True)

test_values = [(0, 'Negativo'), (1, 'Negativo'), (7, 'Negativo'), (12, 'Negativo'), (14, 'Negativo'), (18, 'Negativo'), (27, 'Negativo'), (39, 'Negativo') ,(57, 'Negativo'), (62, 'Negativo'), (82, 'Negativo'), (91, 'Negativo'), (97, 'Negativo'), (452, 'Negativo'), (2198, 'Negativo'), 
(44, 'Positivo') ,(2146, 'Positivo') ,(486, 'Positivo'), (1008, 'Positivo'), (1018, 'Positivo'), (1030, 'Positivo'), (1063, 'Positivo'), (52434, 'Positivo'), (52198, 'Positivo'), (52068, 'Positivo'), 
(2, 'Neutro') ,(3, 'Neutro'), (8, 'Neutro'), (29, 'Neutro'), (70, 'Neutro') ,(76, 'Neutro'), (79, 'Neutro'), (94, 'Neutro'), (690, 'Neutro'), (1041, 'Neutro'), (9650, 'Neutro'), (82213, 'Neutro'), (54455, 'Neutro'), (54360, 'Neutro'), (54313, 'Neutro'), (53418, 'Neutro')]

sorted_by_index = sorted(test_values, key=lambda x: x[0])
list_indexes, list_test_values = zip(*sorted_by_index)

df[['index', 'tweet', 'sentiment_1st','sentiment_2nd']].sort_values('index')

df['sentiment_test'] = list_test_values

#filter = df['index'] in tweets_separados
# df_separado = df[(df['index'].isin(tweets_separados))]
#df_separado['sentiment'] = df_separado['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_pypi((x.replace('[', '').replace(']', '').replace("'", '').replace(',', ''))))
# df['sentiment_2nd'] = df['sentiment_1st']
# df['sentiment_1st'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_pypi(str(x)))
# df[['index', 'tweet', 'sentiment_1st']].sort_values('sentiment_1st')

df.to_csv('./Data/testSentiment.csv')


