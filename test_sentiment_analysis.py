import pandas as pd
import sentimentAnalysis
import tweetFile

df = pd.read_csv('./Datos/vacunasXFraseLimpiasConStopwords.csv')

df['index'] = df['Unnamed: 0']
df.drop(df.columns.difference(['index','tweet']),1,inplace=True)

test_values = [(0, 'Negativo'), (1, 'Negativo'), (7, 'Negativo'), (12, 'Negativo'), (14, 'Negativo'), (18, 'Negativo'), (27, 'Negativo'), (39, 'Negativo') ,(57, 'Negativo'), (62, 'Negativo'), (82, 'Negativo'), (91, 'Negativo'), (97, 'Negativo'), (452, 'Negativo'), (2198, 'Negativo'), 
(44, 'Positivo') ,(2146, 'Positivo') ,(486, 'Positivo'), (1008, 'Positivo'), (1018, 'Positivo'), (1030, 'Positivo'), (1063, 'Positivo'), (52434, 'Positivo'), (52198, 'Positivo'), (52068, 'Positivo'), 
(2, 'Neutro') ,(3, 'Neutro'), (8, 'Neutro'), (29, 'Neutro'), (70, 'Neutro') ,(76, 'Neutro'), (79, 'Neutro'), (94, 'Neutro'), (690, 'Neutro'), (1041, 'Neutro'), (9650, 'Neutro'), (82213, 'Neutro'), (54455, 'Neutro'), (54360, 'Neutro'), (54313, 'Neutro'), (53418, 'Neutro')]

sorted_by_index = sorted(test_values, key=lambda x: x[0])
list_indexes, list_test_values = zip(*sorted_by_index)
df = df[(df['index'].isin(list_indexes))]
df['sentiment_test'] = list_test_values

df['sentiment_value'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_value(str(x)))
df['sentiment_1st'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_discretized_1st(str(x)))
df['sentiment_2nd'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_discretized_2nd(str(x)))
df['sentiment_3rd'] = df['tweet'].map(lambda x: sentimentAnalysis.analize_sentiment_discretized_3rd(str(x)))

accuracy_1st = len(df[(df['sentiment_test'] == df['sentiment_1st'])].index)
accuracy_2nd = len(df[(df['sentiment_test'] == df['sentiment_2nd'])].index)
accuracy_3rd = len(df[(df['sentiment_test'] == df['sentiment_3rd'])].index)
print(accuracy_1st)
print(accuracy_2nd)
print(accuracy_3rd)


accuracy_1st = accuracy_1st/len(list_test_values) * 100
accuracy_2nd = accuracy_2nd/len(list_test_values) * 100
accuracy_3rd = accuracy_3rd/len(list_test_values) * 100

text = "Precision primer test: " + str(accuracy_1st) + "%" + '\n' + "Precision segundo test: " + str(accuracy_2nd) + "%" + '\n' + "Precision tercer test: " + str(accuracy_3rd) + "%"


tweetFile.writeFiles('./Data/testResult.txt', text)
df.to_csv('./Data/testSentiment.csv')


