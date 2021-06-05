import pandas as pd
import sentimentAnalysis
import tweetFile
import test_values

df = pd.read_csv('./Datos/vacunasXFraseLimpiasConStopwords.csv')

df['index'] = df['Unnamed: 0']
df.drop(df.columns.difference(['index','tweet']),1,inplace=True)

sorted_by_index = sorted(test_values.test_values, key=lambda x: x[0])
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


