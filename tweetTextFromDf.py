import pandas as pd
import tweetText
import tweetFile
from_date = '2021-01-23'
to_date = '2021-02-07'
named_vaccine = 'Rusa'
df = pd.read_csv('./Datos/vacunasXFraseNoStopWordsV2.csv')
df['date'] = pd.to_datetime(df['date'])  
df = df[(df['date'] >= from_date) & (df['date'] <= to_date) & (df['named_vaccines'] == named_vaccine)]
all_tweets = tweetText.allText(df['tweet'])
tweetFile.writeFiles('./Tweets/' + named_vaccine + '_' + from_date + '_' + to_date + '.txt', all_tweets)
print('Writed ' + str(len(df.index)) + ' tweets')
