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
from tasks import ManageTasks
from database import ManageDatabase

# start task manager
task_manager = ManageTasks()
task_manager.initialize_class() # init not working?

# start database
database = ManageDatabase()

# generate 10 tasks
for _ in range(1000):
    check_task = True
    while check_task == True:
        # get task
        q_option = random.choice(database.database)
        # select between write and draw
        coin = random.random()
        if coin >= 0.5:
            task = task_manager.gen_task('write',q_option)
        else:
            task = task_manager.gen_task('draw',q_option)

        # check repeated
        check_task = task_manager.check_repeated_task(task)

    # print what we got
    print(task)
