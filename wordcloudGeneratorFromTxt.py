import pandas as pd
import wordcloudJuan
   

def genWordCloud(dates, vaccine):
    i=0
    while(i<len(dates)):
        from_date = dates[i]
        i+=1
        to_date = dates[i]
        i+=1
        named_vaccine = vaccine
        textfileLocation = './Tweets/' + named_vaccine + '_' + from_date + '_' + to_date + '.txt'
        wordcloudLocation = './Wordcloud/twitter/' + named_vaccine + '_' + from_date + '_' + to_date + '.png'
        f = open(textfileLocation, "r+", encoding='utf-8')
        all_tweets = f.read()
        f.close()
        wordcloudJuan.saveWordcloud(all_tweets,wordcloudLocation)
        print('./Wordcloud/twitter/' + named_vaccine + '_' + from_date + '_' + to_date + '.png')



datesRusa = ['2020-08-10',
'2020-08-18', '2020-10-01' , '2020-10-06',
'2020-11-01', '2020-11-08',
'2020-12-15', '2020-12-31',
'2021-01-23', '2021-02-07']

datesChina = ['2020-07-19', 
'2020-07-25',
'2020-11-08', '2020-11-14',
'2021-01-02', '2021-01-16',
'2021-03-01', '2021-03-14',
'2021-04-08', '2021-04-17']

genWordCloud(datesRusa, 'Rusa')