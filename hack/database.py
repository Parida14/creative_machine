#!/usr/bin/env python
"""database.py: database for q_option
"""

__author__ = "Vinicius Guimaraes Goecks"
__copyright__ = "TBD"
__collaborators__ = ["Mauricio Coen", "Aniket Bonde", "Lagnajit Parida"]
__license__ = "TBD"
__version__ = "0.0.0"
__maintainer__ = "Vinicius Guimaraes Goecks"
__email__ = "viniciusguigo@gmail.com"
__status__ = "Prototype"
__date__ = "October 29, 2016"

# import

class ManageDatabase():
    """
    Manages the database of q_option.
    """
    def __init__(self):
        # initialize self
        self.new_database = []
        self.learning_database = self._load_learning_set()

    def _load_learning_set(self):
        """
        Base q_options.
        """
        q_option = ["foods",
                    "animals",
                    "colors",
                    "pets",
                    "seasons"]

        return q_option

def init_text():
    """
    Print basic info about the app.
    """
    print("*** Hello, welcome to the Creative Machine! (v1.1) ***")
    print("\nHave you ever heard about Creative Therapy?")
    print("\nCreative therapy refers to a group of techniques that are expressive")
    print("and creative in nature. The aim of creative therapies is to help")
    print("clients find a form of expression beyond words or traditional therapy,")
    print("such as cognitive or psychotherapy.")
