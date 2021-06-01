import pandas as pd
import wordcloudJuan
import tweetText
import categorizer

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

usernames = ['notidesalta','infocastellana','rosariotres', 'diariotalcual','agenciatelam',
 'hispanopost', 'cactus24noticia', 'diarioquepasa', 'pagina12', 'tvnnoticias', 'contexto_tuc', 
'foro_tv', 'perfilcom','diariopanorama', 'nucleonoticias', 'vocesdiario', 'elcomercio_peru', 'elcomunistanet',
'noticiasprensa', 'infobaeamerica', 'venezuelaaldia', 'telesurtv', 'lanacion', 'peruenlanoticia', 'cronica',
'clarincom', 'entornoint', 'larepublica_pe', 'diariocontraste', 'infopublicave', 'globovision', 'tulionoticias',
'elperiodiquito', 'radiodogo', 'notifalcon', 'infobae', 'noticierovv', 'elpoliticonews' , 'contrapuntovzla',
'elpitazotv', 'sunoticiero' , 'conelmazodando', 'eldiario', 'eldolardiario', 'actualidadrt', 'nxvenezuela',
'caraotadigital', 'elportal24', 'mhidrovia', 'maduradascom', 'elnacionalweb', 'portaldiarioar', 'el_cooperante',
'la_patilla']


df = pd.read_csv('./Datos/vacunasXFraseNoStopWordsV2.csv')

i=0
while(i<len(datesChina)):
        from_date = datesChina[i]
        i+=1
        to_date = datesChina[i]
        i+=1
        
        named_vaccine = 'China'
        
        df_selected = df[(df['date'] >= from_date) & (df['date'] <= to_date) 
        & (df['named_vaccines'] == named_vaccine) & (df['username'].isin(usernames))]
        
        all_tweets = tweetText.allText(df_selected['tweet'])

        wordcloudLocation = './Wordcloud/News/' + named_vaccine + '_' + from_date + '_' + to_date + '.png'
        
        wordcloudJuan.saveWordcloud(all_tweets,wordcloudLocation)
        print('./Wordcloud/News/' + named_vaccine + '_' + from_date + '_' + to_date + '.png')



