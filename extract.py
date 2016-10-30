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
