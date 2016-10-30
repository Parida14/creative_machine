#!/usr/bin/env python
"""manage_input.py:
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
import random

class ManageInputs():
    """
    This class manage inputs, generate learning questions, etc.
    """

    def __init__(self):
        self.size_input = 0

    def gen_learning_question(self, q_learning_option):
        """
        Generate learning questions based on the learning database.

        Input
        ----------
        q_learning_option = keyword from the standard learning_database
        """
        learning_question = ["tell me about your favorite ",
                             "what do you think about "]
        select_question = random.choice(learning_question)

        question = select_question + q_learning_option

        return question
