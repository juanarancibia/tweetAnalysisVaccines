import pandas as pd
import sentimentAnalysis

df = pd.read_csv('./Datos/vacunasXFraseSentimientosConStopwords.csv')
df['index'] = df['Unnamed: 0']


tweets_separados = [0, 1, 7, 12, 14, 18, 27, 39 ,57, 62, 82, 91, 97, 452, 2198, 
44 ,2146 ,486, 1008, 1018, 1030, 1063, 52434, 52198, 52068, 
2 ,3, 8, 29, 70 ,76, 79, 94, 690, 1041, 9650, 82213, 54455, 54360, 54313, 53418]


#filter = df['index'] in tweets_separados
df_separado = df[(df['index'].isin(tweets_separados))]
df_separado['sentiment'] = df_separado['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_pypi((x.replace('[', '').replace(']', '').replace("'", '').replace(',', ''))))
print(df_separado[['index','sentiment']].sort_values('sentiment'))


