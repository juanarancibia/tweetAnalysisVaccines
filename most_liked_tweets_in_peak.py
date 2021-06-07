import pandas as pd

dates = ['2020-08-10', '2020-08-18',
'2020-10-01', '2020-10-06',
'2020-11-01', '2020-11-08',
'2020-12-15', '2020-12-31',
'2021-01-23', '2021-02-07',
'2020-07-19', '2020-07-25',
'2020-11-08', '2020-11-14',
'2021-01-02', '2021-01-16',
'2021-03-01', '2021-03-14',
'2021-04-08', '2021-04-17']

df = pd.read_json('./Datos/vacunasXFrase.json')
df.drop(df.columns.difference(['username', 'tweet', 'date', 'likes_count', 'retweets_count', 'replies_count', 'link']),1,inplace=True)
df['popularity'] = (df['likes_count'] + df['retweets_count'] + df['replies_count']) /3
i=0
while(i<len(dates)):
    from_date = dates[i]
    i+=1
    to_date = dates[i]
    i+=1
    
    df_dates = df[(df['date'] >= from_date) & (df['date'] <= to_date)]
    popularDf = df_dates.sort_values(by=['popularity'], ascending=False).head(1000)
    
    popularDf.to_csv(f'./Data./peak_liked_tweets/liked_{from_date}_to_{to_date}.csv')
