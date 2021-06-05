from collections import Counter

def detectTrollTweets(tweets):
    alltweetsDictionary = dict(Counter(tweets))
    filteredTweets = alltweetsDictionary.copy()
    for tweet in alltweetsDictionary:
        if ((alltweetsDictionary[tweet] <= 10)):
           del filteredTweets[tweet]
    print(dict(sorted(filteredTweets.items(), key=lambda item: item[1])))
    return dict(sorted(filteredTweets.items(), key=lambda item: item[1],reverse=True))

def getTrollsUsername(df):
    trollsDict = {}

