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
        q_option = ["food",
                    "animal",
                    "country",
                    "color",
                    "pet",
                    "red",
                    "season"]

        return q_option
