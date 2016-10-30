#!/usr/bin/env python
"""test_run.py: quick task run for the app
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
from extract import get_nouns
from tasks import ManageTasks
from database import ManageDatabase
from manage_input import ManageInputs

# parameters
number_of_days = 5

# initialize all
input_manager = ManageInputs()
task_manager = ManageTasks()
task_manager.initialize_class() # init not working?

database = ManageDatabase()

input_data = ManageInputs()

# repeat for each day
for day in range(number_of_days):
    print("\n*** Day %i ***" %day)

    # get input (ask learning questions)
    check_input = True
    count_input = 0
    while check_input == True: # make sure it is not repeated
        q_option = random.choice(database.learning_database)
        input_question = input_data.gen_learning_question(q_option)

        # check repeated
        check_input = input_manager.check_repeated_inputs(input_question)
        count_input += 1
        # try 10 times
        if count_input >= 3:
            input_question = "No questions this time!"
            check_input = False
            break

    # ask input
    if input_question == "No questions this time!":
        print("No questions this time!")
    else:
        # get input
        user_input = input(input_question+": ")

        # extract nouns and send to new database
        new_nouns = get_nouns(user_input)
        for each_entry in new_nouns:
            database.new_database.append(each_entry)

    # clean duplicates on new database
    database.new_database = list(set(database.new_database))

    # get answer (from task)
    # select between write and draw
    check_task = True
    count_task = 0
    if len(database.new_database): # check if empty
        while check_task == True: # make sure it is not repeated
            q_new_option = random.choice(database.new_database)
            coin = random.random()
            if coin >= 0.5:
                task = task_manager.gen_task('write',q_new_option)
            else:
                task = task_manager.gen_task('draw',q_new_option)

            # check repeated
            check_task = task_manager.check_repeated_task(task)
            count_task += 1
            # try 10 times
            if count_task >= 3:
                task = "No questions this time!"
                check_task == False
                break

        # ask the task
        if task == "No questions this time!":
            print("No questions this time!")
        else:
            task_answer = input(task+": ")

    else:
        print("No task this time!")

# add new nouns to database

# # generate 10 tasks
# for _ in range(1000):
#     check_task = True
#     while check_task == True:
#         # get task
#         q_option = random.choice(database.learning_database)
#         # select between write and draw
#         coin = random.random()
#         if coin >= 0.5:
#             task = task_manager.gen_task('write',q_option)
#         else:
#             task = task_manager.gen_task('draw',q_option)
#
#         # check repeated
#         check_task = task_manager.check_repeated_task(task)
#
#     # print what we got
#     print(task)
