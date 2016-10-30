#!/usr/bin/env python
"""tasks.py: work on questins for the creative machine
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


class ManageTasks():
    """
    Manage everything related to the tasks.

    Methods
    ---------
    gen_task = generates new tasks
    check_repeated_task = i will let you guess that
    """

    def ___init___(self):
        self.tasks_asked = []  # empty list of tasks asked

    def initialize_class(self):
        self.tasks_asked = []  # empty list of tasks asked

    def gen_task(self, q_type, q_option):
        """
        Generate tasks based on inputs.

        Inputs
        ---------
        type = write, draw (action to be proposed)
        option = item (the categorie to be asked about)

        Outputs
        ---------
        task = string with task
        data = output the selected q_type and q_option from the database to
               create a future list and block repeated tasks.
        """
        # check what it the task about
        if q_type == "write":
            question = ["Please, let me know what you most like on ",
                        "Please, write a short sentence about ",
                        "Please, write the first experience you had with "]
            select_question = random.choice(question)

        elif q_type == "draw":
            draw = [
                "In a separeted piece of paper, please draw your favorite ",
                "In a separeted piece of paper, please draw the first thing it comes to your mind when you think about "
            ]
            select_question = random.choice(draw)

        # output the task based on the option input
        select_option = q_option

        # join everything
        task = select_question + select_option

        return task

    def check_repeated_task(self, task):
        """
        Check if this was already asked.

        Inputs
        ---------
        task = string containing q_type+q_option

        Outputs
        ---------
        task_status = if asked or not (False, True)
        """
        task_status = task in self.tasks_asked

        # append if never asked
        if task_status == False:
            self.tasks_asked.append(task)

        return task_status

    def get_task_answer(answer):
        """
        This method will receive the answer from the user
        """
        self.task_answer = answer
