#!/usr/bin/env python
"""test_run.py: quick task run for the app
"""

__author__ = "Vinicius Guimaraes Goecks"
__copyright__ = "TBD"
__collaborators__ = ["Mauricio Coen", "Aniket Bonde", "Lagnajit Parida"]
__license__ = "TBD"
__version__ = "1.1"
__maintainer__ = "Vinicius Guimaraes Goecks"
__email__ = "viniciusguigo@gmail.com"
__status__ = "Prototype"
__date__ = "October 29, 2016"

# import
import random
import numpy as np
from extract import get_nouns, sentiment_analysis, report_sentiment
from tasks import ManageTasks
from database import ManageDatabase, init_text
from manage_input import ManageInputs
from test_json import output_to_json

# parameters
number_of_days = 3
sentiment_data = np.zeros((number_of_days,3))   # for sentiment analysis
questions_selected = [] # save questions asked
answers_given = []      # answers_given by the user

# initialize all
input_manager = ManageInputs()
task_manager = ManageTasks()
task_manager.initialize_class()  # init not working?
database = ManageDatabase()
input_data = ManageInputs()

# initial menu
init_text()
print("\nFor this demo we will be simulating the activity for %i consecutive days." %number_of_days)
print("On the final app you are supposed to complete only task a day. Take it easy :)")
print("The important part is HOW you complete the task! Not the quantity.")
username = input("\nWhen you are ready to start, please let me know how should I call you: ")

# repeat for each day
for day in range(number_of_days):
    print("\n*** Day %i ***" % day)

    # get input (ask learning questions)
    check_input = True
    count_input = 0
    while check_input == True:  # make sure it is not repeated
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
        print("\n- Help me to learn more about you, %s! -" %username)
        user_input = input(input_question + ": ")

        # save the data and send to json
        questions_selected.append(input_question)
        output_to_json(input_question)

        answers_given.append(user_input)
        output_to_json(user_input)

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
    if len(database.new_database):  # check if empty
        while check_task == True:  # make sure it is not repeated
            q_new_option = random.choice(database.new_database)
            coin = random.random()
            if coin >= 0.5:
                task = task_manager.gen_task('write', q_new_option)
                mode = 'write'
            else:
                task = task_manager.gen_task('draw', q_new_option)
                mode = 'draw'

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
            print("\n- Here's my task to help you being more creative: -")
            task_answer = input(task + ": ")

            # save the data
            questions_selected.append(task)
            output_to_json(task)

            answers_given.append(task_answer)
            output_to_json(task_answer)

            # extract sentiment
            if mode == 'write':
                p,s = sentiment_analysis(task_answer)
                sentiment_data[day,:] = [p, s, day]

    else:
        print("No task this time!")

    # save questions asked and answers


# execute a final report based on sentiment analysis
report_sentiment(sentiment_data)
