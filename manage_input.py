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
        self.inputs_asked = [] # empty list of tasks asked

    def gen_learning_question(self, q_learning_option):
        """
        Generate learning questions based on the learning database.

        Input
        ----------
        q_learning_option = keyword from the standard learning_database
        """
        learning_question = ["Please, let me know your favorite ",
                             "Please, let me know what you think about ",
                             "Please, write the first thing that comes to your mind when you think about "]
        select_question = random.choice(learning_question)

        question = select_question + q_learning_option

        return question

    def check_repeated_inputs(self, user_input):
        """
        Check if this was already asked.

        Inputs
        ---------
        inputs = string containing inputs

        Outputs
        ---------
        inputs_status = if asked or not (False, True)
        """
        input_status = user_input in self.inputs_asked

        # append if never asked
        if input_status == False:
            self.inputs_asked.append(user_input)

        return input_status
