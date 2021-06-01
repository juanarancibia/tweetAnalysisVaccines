from typing import Counter

from PIL import Image, ImageFilter
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from palabrasASacar import stopwords_common
import numpy as np

def generateWordcloud(text):
    mask = np.array(Image.open("./WordCloud/twitter-mask.png"))
    wordcloud = WordCloud(stopwords = stopwords_common, background_color="lightblue",width=2040, height=1080, max_words=50, mask=mask, contour_width=5, contour_color='black',relative_scaling=1).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def saveWordcloud(text, fileLocation):
    mask = np.array(Image.open("./WordCloud/virus-mask.png"))
    wordcloud = WordCloud(stopwords = stopwords_common, background_color="lightblue",width=2040, height=1080, max_words=1000, mask=mask, contour_width=5, contour_color='black',relative_scaling=0).generate(text)
    wordcloud.to_file(fileLocation)


def mostCommon(text):
    cnt = Counter()
    text = text.split()
    for word in text:
        cnt[word] += 1
    mostCommon = dict(cnt.most_common(2000))
    print(mostCommon.keys())
