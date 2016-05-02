#!/usr/bin/env python3.5

#import os

from os import listdir 
from os import getcwd
from os import chdir
from os import rename 

def rename_files():
    print ("\nBegin rename_files function\n")

    # get the current working directory
    save_path = getcwd()
    # print('save_path is -> {}'.format(save_path)) - works 
    # print('save_path is -> {}\n'.format(getcwd())) - works 
    # print('current working dir is -> {}\n'.format(getcwd())) - works

    # change dir to where the files are
    # location of files to be renamed 
    chdir("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/prank")
    # print('files to be renamed location - dir - is -> {}\n'.format(getcwd()))
    
    # get the files to be renamed 
    # os.listdir("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/prank")
    file_list = listdir("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/prank")

    # print(file_list)
    # print ("\tfile_list is -> %s" % file_list)

    for file_name in file_list:
        
        # print(file_name)
        print('file_name is -> {}'.format(file_name)) 

        # from instructor
        # possibly older python version - did not work 
        # file_name.translate(None, '0123456789')
        
        # works 
        numbersGone = ''.join(i for i in file_name if not i.isdigit())
        print('numbersGone is -> {}\n'.format(numbersGone))
 
        x = rename(file_name, numbersGone)
        # print ("x class name is\t= %s\n" % x.__class__.__name__)
        # x class name is	= NoneType

        # change dir to where the files are
        # location of files to be renamed 
        # chdir("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/prank")
        # print('new current working dir is -> {}\n'.format(getcwd()))

        # print('current working dir is -> {}\n'.format(getcwd()))

        # /Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016 - python source here
        # /Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/prank - files here 

        # print()

    print('files to be renamed location - dir - is -> {}'.format(getcwd()))
    print('save_path is -> {}'.format(save_path))
    chdir(save_path)
    print('restored working dir is -> {}\n'.format(save_path))

    print ("End rename_files function\n")

print ("\nBegin rename_files.py module")

rename_files()

print ("End rename_files.py module\n")


# works
#import os
#os.listdir("foo")

# works
# from os import listdir
# listdir("foo")








##
###
### Python Standard Library
###   file (module) name webbrowser   - function - def open
###   file (module) name time         - function - def ctime ; def sleep
###
###
### import time module
##import time
##
### import webbrowser module
##import webbrowser
##
##total_breaks = 2
##break_count = 0
##
##print ("\nStarted break_time.py module")
##
##while (break_count < total_breaks):
##    print ("\nBefore open Webbrowser" + time.ctime())
##
##    time.sleep(5)
##    webbrowser.open("https://www.youtube.com/watch?v=PSKQ3ZNQ_O8")
##    break_count = break_count + 1
##
##    print('break_count is -> {}'.format(break_count))
##    print ("End open Webbrowser")
##
##
##print ("\nEnded break_time.py module\n")
###print()
##
##
### print ("Before open Webbrowsr")
##
##
### print ("End open Webbrowsr")
##
##
##
 




 
