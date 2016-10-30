#!/usr/bin/env python
"""test_run.py: quick task run for the app
"""

__author__ = "Aniket Bonde"
__copyright__ = "TBD"
__collaborators__ = ["Vinicius Guimaraes Goecks", "Mauricio Coen",
                     "Lagnajit Parida"]
__license__ = "TBD"
__version__ = "0.0.0"
__maintainer__ = "Vinicius Guimaraes Goecks"
__email__ = "viniciusguigo@gmail.com"
__status__ = "Prototype"
__date__ = "October 29, 2016"

# import
from textblob import TextBlob
import matplotlib.pyplot as plt


def get_nouns(text):
    """
    Extract nouns from text
    """
    # classify words as nouns, verbs, etc
    blob = TextBlob(text)
    list_nouns = []

    # just get the nouns
    for word, pos in blob.tags:
        if (pos == 'NNS' or pos == 'NNP' or pos == 'NNPS' or pos == 'NN'):
            list_nouns.append(word)

    return list_nouns

def sentiment_analysis(text):
    """
    Extract sentiment (from -1 to 1, in terms of being positive) and level of
    emotion (from 0 to 1)

    Input
    ----------
    text = text to be analysed

    Output
    ----------
    p = sentiment level
    s = level of emotion
    """
    p, s = TextBlob(text).sentiment
    return p, s

def report_sentiment(sentiment_data,dict_polarity,dict_subjectivity):
    """
    After complete the whole activity, create a small report based on the
    sentiment collected.
    """
    p = sentiment_data[:,0]
    s = sentiment_data[:,1]
    day = sentiment_data[:,2]

    # sort ranking
    pol_sorted_list = sorted(dict_polarity, key=lambda key: dict_polarity[key])
    sub_sorted_list = sorted(dict_subjectivity, key=lambda key: dict_subjectivity[key])

    # print ranking
    # print(pol_sorted_list)

    # plot sentiment and subjectivity
    plt.figure()
    plt.title('Sentiment Analysis by Day')
    plt.xlabel('Day')
    plt.plot(day, p,'rx-',label='polarity')
    plt.plot(day, s,'bo-',label='subjectivity')
    plt.ylim(-1,1)
    plt.legend()
    plt.grid()

    plt.show()
