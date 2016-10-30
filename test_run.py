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
from tasks import ManageTasks

# start task manager
task_manager = ManageTasks()
task_manager.initialize_class() # init not working?

# generate 10 tasks
for _ in range(10):
    check_task = True
    while check_task == True:
        # get task
        task = task_manager.gen_task('draw','cat')

        # check repeated
        check_task = task_manager.check_repeated_task(task)

    # print what we got
    print(task)
