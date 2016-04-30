#!/usr/bin/env python3.5
#
# Python Standard Library
#   file (module) name webbrowser   - function - def open
#   file (module) name time         - function - def ctime ; def sleep
#
#
# import time module
import time

# import webbrowser module
import webbrowser

total_breaks = 2
break_count = 0

print ("\nStarted break_time.py module")

while (break_count < total_breaks):
    print ("\nBefore open Webbrowser" + time.ctime())

    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=PSKQ3ZNQ_O8")
    break_count = break_count + 1

    print('break_count is -> {}'.format(break_count))
    print ("End open Webbrowser")


print ("\nEnded break_time.py module\n")

