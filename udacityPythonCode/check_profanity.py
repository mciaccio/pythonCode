#!/usr/bin/env python3.5

import time
import webbrowser
import sys
import urllib
import urllib.request
#import urllib2

# quotes = ""
contents_of_file = None


print("\nBegin check_profanity module\n")
# http://www.purgomalum.com/service/json?text=this is some test 

def read_text():
    
    print("Begin read_text() function\n")

    # reference the global scoped (module wide) variable, not a function scoped variable
    global contents_of_file
    
    # quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udaCityPythonCode/profEditor/movie_quotes.txt", encoding='utf-8')
    # quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udaCityPythonCode/profEditor/movie_quotes.txt")
    quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/profanity/movie_quotes.txt")

    # drilling down into an object
    # get methods
    # print ("dir(quotes)")
    # print (dir(quotes))
    # print()
    
    # print ("quotes")
    # print (quotes)
    # print()
    
    # drilling down into an object, dot notation
    print ("quotes class name is\t= %s" % quotes.__class__.__name__)
    # quotes class name is	= TextIOWrapper

    print ("name \t\t\t=  %s" % quotes.name)
    # name =  /Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udacityPythonCode2016/profanity/movie_quotes.txt

    print ("mode \t\t\t=  %s" % quotes.mode)
    # mode =  r

    print ("encoding \t\t=  %s\n" % quotes.encoding)
    # encoding =  US-ASCII

    # contents of local text file
    contents_of_file = quotes.read()
    
    print("global contents_of_file is \n%s" % contents_of_file)
    
    quotes.close()        
    print("End read_text() function")


def check_profanity(text_to_check):
    print("Begin check_profanity() function\n")

    # works - make sure running right file
    print (urllib.__file__) 
    # /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/__init__.py

    # works - make sure running right file
    print (urllib.request.__file__) 
    # /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py
    print()

    # get attributes and methods
    # print(dir(urllib)) 
    # print()
    
    # get attributes and methods
    # print(dir(urllib.request))
    # print()

    # contents of local text file contents_of_file - text_to_check
    print ("text_to_check class name is\t= %s\n" % text_to_check.__class__.__name__)
    # text_to_check class name is	= str
    # print()

    # one way to clean up url
    my_text_to_check = text_to_check.replace(' ', '%20')
    # print("my_text_to_check is - \n%s" % my_text_to_check)
    # print()

    # one way to clean up url
    my_text_to_check = my_text_to_check.replace('\n', '%20.')
    print("my_text_to_check is - \n%s" % my_text_to_check)
    print()

    myURL = ("http://www.purgomalum.com/service/containsprofanity?text=" + my_text_to_check)
    print("myURL is %s " % myURL)
    # myURL is http://www.purgomalum.com/service/containsprofanity?text=
    # Houston,%20we%20have%20a%20problem.%20(Apollo%2013)%20.%20.
    # Mama%20always%20said,%20life%20is%20like%20a%20box%20of%20chocolates.%20You%20never%20know%20what%20you%20are%20going%20to%20get.%20
    # (Forrest%20Gump)%20.%20.
    # You%20cant%20handle%20the%20truth.%20(A%20Few%20Good%20Men)%20.%20.
    # I%20believe%20everything%20and%20I%20believe%20nothing.%20(A%20Shot%20in%20the%20Dark)%20. 
    print()

    my_HTTPResponse = urllib.request.urlopen(myURL)
    print ("my_HTTPResponse class name is\t= %s" % my_HTTPResponse.__class__.__name__)
    # my_HTTPResponse class name is	= HTTPResponse
    print()

    my_bytes = my_HTTPResponse.read()
    print ("my_bytes class name is\t= %s" % my_bytes.__class__.__name__)
    # my_bytes class name is	= bytes
    
    print("my_bytes is %s " % my_bytes)
    # my_bytes is b'false' 
    print()
 
    print("profanity_result ascii is %s" % my_bytes.decode('ascii'))
    # profanity_result ascii is false
    
    print("profanity_result utf-8 is %s" % my_bytes.decode('utf-8'))
    # profanity_result utf-8 is false
    print()

    my_HTTPResponse.close()
    
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").code) # 200
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").msg)  # OK
    print()

    # no real value 
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck"))
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").__str__)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").getcode)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").getheader)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").getheaders)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").geturl)
    
    # print(dir(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read))
    # print()

    #print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read)
    # print()
    
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__str__)
    # print()
    
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__sizeof__)
    # print()

    #print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read1)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__get__) # no real value
    
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read(100))        # b'false'
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").readline(100))    # b'false'
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").readlines(100))   # [b'false']
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read1(100))       # b'false'
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=shit").read1(100))       # b'true' - note profane 

    # use case url has hard coded space 
    # urllib.error.HTTPError: HTTP Error 400: Bad Request - note space - text= shot 
    # x = "http://www.purgomalum.com/service/containsprofanity?text= shot"
    # print(x)
    # http://www.purgomalum.com/service/containsprofanity?text= shot - note the space 
    # print(urllib.request.urlopen(x).read(100) )
    # can't open it - urllib.error.HTTPError: HTTP Error 400: Bad Request
    # print()

    # use case url has %20 hard coded - space encoded - %20
    x = "http://www.purgomalum.com/service/containsprofanity?text=shot%20shot1%20shit"
    print("zzz")
    print(x)
    # http://www.purgomalum.com/service/containsprofanity?text=shot%20shot1%20shit
    print(urllib.request.urlopen(x).read(100))
    # b'true'
    print()
    
    # use case hard coded space and profanity 
    x = "http://www.purgomalum.com/service/containsprofanity?text=shot%20shot1 shit"
    print(x)
    # http://www.purgomalum.com/service/containsprofanity?text=shot%20shot1 shit
    # print(urllib.request.urlopen(x).read(100))
    # urllib.error.HTTPError: HTTP Error 400: Bad Request
    print()

    # *** url cleanup - urllib.parse.quote(x, safe="%/:=&?~#+!$,;'@()*[]") *** 
    # use case hard coded space and profanity
    # urllib.parse.quote - cleans up url - works 
    x = "http://www.purgomalum.com/service/containsprofanity?text=shot shot1 shit"
    print(x)
    # http://www.purgomalum.com/service/containsprofanity?text=shot shot1 shit
    x = (urllib.parse.quote(x, safe="%/:=&?~#+!$,;'@()*[]"))
    print(x)
    # http://www.purgomalum.com/service/containsprofanity?text=shot%20shot1%20shit - url cleaned up - note %20
    print(urllib.request.urlopen(x).read(100))
    # b'true' - true profanity present 

    print("\nEnd check_profanity() function")
    
### Begin check_profanity.py module ###

print ("sys.version is %s\n" % sys.version)

read_text()
check_profanity(contents_of_file)

print('\nEnd check_profanity module\n')



# comment
"""
multi line comment
line 2
"""


 

