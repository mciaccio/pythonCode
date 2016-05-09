#!/usr/bin/env python3.5

# import urllib
import urllib.request

def read_text():
    print ("\tBegin read_text function\n")
    quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/profanity/movie_quotes.txt")
    
    # print('\tquotes is -> {}\n'.format(quotes))

    print('\tquotes.__class__ is -> {}'.format(quotes.__class__))
    print('\tquotes.__class__.__name__ is -> {}\n'.format(quotes.__class__.__name__)) 
    # print('\tdir(quotes) is -> {}\n'.format(dir(quotes)))

    contents_of_file = quotes.read()
    # print('\tcontents_of_file is ->')
    # print('{}'.format(contents_of_file))jjjj
    # print(format(contents_of_file))

    # built ins 
    # https://docs.python.org/3/library/functions.html
    # print built in globals
    # print('\tglobals() is -> {}\n'.format(globals()))

    # print built in locals
    # print('\tlocals() is -> {}\n'.format(locals())) 
 
    # for line in quotes:
    #    print('\tline is -> {}\n'.format(line))

    quotes.close()

    # check_profanity("Shit")
    check_profanity(contents_of_file)
    # check_profanity("Houston, we have a problem. (Apollo 13)")
    # check_profanity("Houston, we")

    print ("\tEnd read_text function\n")

def check_profanity(text_to_check):
    print ("\tBegin check_profanity function\n")
    
    print('\ttext_toCheck is -> {}\n'.format(text_to_check))
    # fixed_text_to_check = text_to_check
    fixed_text_to_check = urllib.parse.quote(text_to_check, safe="%/:=&?~#+!$,;'@()*[]")
    print('\tfixed_text_to_check is -> {}\n'.format(fixed_text_to_check))

    # connection = urllib.request.urlopen("http://www.google.com")
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + fixed_text_to_check)

    # print('\tdir(connection) is -> {}\n'.format(dir(connection)))
    
    print('\tconnection.__class__ is -> {}'.format(connection.__class__))
    print('\tconnection.__class__.__name__ is -> {}'.format(connection.__class__.__name__))
    
    print('\n\tconnection.status is -> {}'.format(connection.status))
    print('\tconnection.reason is -> {}\n'.format(connection.reason))

    output = connection.read()
    # output = "hard coded"
    # output is -> b'false'

    # output = connection.read1()
    # output is -> b'false'
    
    # output = connection.readline()
    # output is -> b'false'
 
    print('\toutput.__class__ is -> {}'.format(output.__class__))
    print('\toutput.__class__.__name__ is -> {}\n'.format(output.__class__.__name__))

    print('\toutput is -> {}\n'.format(output))
 
    connection.close()
    print ("\tEnd check_profanity function\n")
    

print ("\nBegin check_profanity.py python module\n")

read_text()
# check_profanity("shot")

print ("End check_profanity.py python module\n")




