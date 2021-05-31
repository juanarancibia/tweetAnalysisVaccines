from collections import Counter

def detectTrollTweets(tweets):
    alltweetsDictionary = dict(Counter(tweets))
    filteredTweets = alltweetsDictionary.copy()
    for tweet in alltweetsDictionary:
        if ((alltweetsDictionary[tweet] <= 20)):
           del filteredTweets[tweet]
    print(dict(sorted(filteredTweets.items(), key=lambda item: item[1])))
    return filteredTweets

def getTrollsUsername(df):
    trollsDict = {}

