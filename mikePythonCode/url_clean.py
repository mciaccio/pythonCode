#!/usr/bin/env python3.5

import time
import webbrowser
import sys
import urllib
import urllib.request
#import urllib2

# quotes = ""
contents_of_file = None


print("\nBegin url_clean module\n")
# http://www.purgomalum.com/service/json?text=this is some test
# http://www.purgomalum.com/service/json?text=this is some test

# http://www.purgomalum.com/service/containsprofanity?text=this is some test input as

def read_text():
    
    print("Begin read_text() function\n")

    # reference the global scoped (module wide) variable, not a function scoped variable
    global contents_of_file
    
    #quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udaCityPythonCode/profEditor/movie_quotes.txt", encoding='utf-8')
    quotes = open("/Users/MenfiSystems/Documents/machineLearning/python/pythonCode/udaCityPythonCode/profEditor/movie_quotes.txt")

    # drilling down into an object
    
    print ("dir(quotes)")
    print (dir(quotes))
    print()
    
    print ("quotes")
    print (quotes)
    print()
    
    # drilling down into an object, dot notation
    print ("quotes class name is\t= %s" % quotes.__class__.__name__)
    print ("name \t\t\t=  %s" % quotes.name)
    print ("mode \t\t\t=  %s" % quotes.mode)
    print ("encoding \t\t=  %s\n" % quotes.encoding)

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

    # get attributes and methods, see what we are dealing with
    print(dir(urllib)) 
    print()
    
    # get attributes and methods, see what we are dealing with
    print(dir(urllib.request))
    print()

    # contents of local text file contents_of_file - text_to_check
    print ("text_to_check class name is\t= %s\n" % text_to_check.__class__.__name__)
    # print("text_to_check is - \n%s" % text_to_check)
    # print()

    my_text_to_check = text_to_check.replace(' ', '%20')
    # print("my_text_to_check is - \n%s" % my_text_to_check)
    # print()

    my_text_to_check = my_text_to_check.replace('\n', '%20.')
    print("my_text_to_check is - \n%s" % my_text_to_check)
    print()


    myURL = ("http://www.purgomalum.com/service/containsprofanity?text=" + my_text_to_check)
    print("myURL is %s " % myURL)
    print()

    my_HTTPResponse = urllib.request.urlopen(myURL)
    print ("my_HTTPResponse class name is\t= %s" % my_HTTPResponse.__class__.__name__)
    print()

    my_bytes = my_HTTPResponse.read()
    print ("my_bytes class name is\t= %s" % my_bytes.__class__.__name__)
    print("my_bytes is %s " % my_bytes)
    print()
 
    print("profanity_result ascii is %s" % my_bytes.decode('ascii'))
    print("profanity_result utf-8 is %s" % my_bytes.decode('utf-8'))
    print()

    my_HTTPResponse.close()
    
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").code)
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").msg)
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
    
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read)
    # print()
    
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__str__)
    # print()
    
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__sizeof__)
    # print()

    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read1)
    # print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read.__get__)
    # no real value
    
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read(100))
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").readline(100))
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").readlines(100))
  
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=duck").read1(100))
    print(urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=shit").read1(100))

    print("\nEnd check_profanity() function")

def url_clean_function():
    print("Begin url_clean_function\n")

    # not much value
    print(urllib.request.urlopen("https://www.google.com/?gws_rd=ssl#q=toys+cars"))
    # <http.client.HTTPResponse object at 0x1057d3438>
 
    # space in url toys space cars
    # urllib.error.HTTPError: HTTP Error 400: Bad Request expected but not seen -
    # google.com fixes it - note %20
    # https://www.google.com/?gws_rd=ssl#q=toys%20cars 
    my_HTTPResponse = urllib.request.urlopen("https://www.google.com/?gws_rd=ssl#q=toys cars")
    print ("my_HTTPResponse class name is\t= %s" % my_HTTPResponse.__class__.__name__)
    # my_HTTPResponse class name is	= HTTPResponse
    print()

    # not much value 
    print ("my_HTTPResponse is\t= %s" % my_HTTPResponse)
    # my_HTTPResponse is	= <http.client.HTTPResponse object at 0x105822e80>
    print()

    # prints attributes (dir) of the class 
    print ("dir(my_HTTPResponse) %s" % dir(my_HTTPResponse))
    print()

##    each call gets the next 5, the same 5 are not returned each time
    
##    print ("my_HTTPResponse.read(5) %s" % my_HTTPResponse.read(5))
##    print()
##    print ("my_HTTPResponse.read(5) %s" % my_HTTPResponse.read(5))
##    print()
##    print ("my_HTTPResponse.read(5) %s" % my_HTTPResponse.read(5))
##    print()

    # get the first 2 bytes
    my_first_two_bytes = my_HTTPResponse.read(2)
    print ("my_first_two_bytes are %s" % my_first_two_bytes)
    # my_first_two_bytes are b'<!'
    print()

    print ("my_first_two_bytes.decode('ascii') is %s" % my_first_two_bytes.decode('ascii'))
    # my_first_two_bytes.decode('ascii') is <!
    print()

    # get bytes 3 - 28
    print ("my_HTTPResponse.read1(25) %s" % my_HTTPResponse.read1(25))
    # my_HTTPResponse.read1(25) b'doctype html><html itemsc'
    print()
    
    # HTTPResponse class - readlines method - returns all of it
    #print ("my_HTTPResponse.readlines() %s" % my_HTTPResponse.readlines())
    # print()

    # HTTPResponse class - readlines method - returns 1 line
    print ("my_HTTPResponse.readlines(1) %s" % my_HTTPResponse.readlines(1))
    print()

    # returns the headers
    print ("my_HTTPResponse.getheaders() %s" % my_HTTPResponse.getheaders())
    print()

    # returne a header
    print ("my_HTTPResponse.getheader('Content-Type') %s" % my_HTTPResponse.getheader('Content-Type'))
    # my_HTTPResponse.getheader('Content-Type') text/html; charset=ISO-8859-1
    print()

    print ("my_HTTPResponse.msg is\t\t= %s" % my_HTTPResponse.msg)
    # my_HTTPResponse.msg is		= OK
    print()

    print ("my_HTTPResponse.status is\t= %s" % my_HTTPResponse.status)
    # my_HTTPResponse.status is	= 200
    print()

    
    print ("my_HTTPResponse.reason is\t= %s" % my_HTTPResponse.reason)
    # my_HTTPResponse.reason is	= OK
    print()
    
    print ("my_HTTPResponse.version is\t= %s" % my_HTTPResponse.version)
    #my_HTTPResponse.version is	= 11
    print() 

    # works no space in url
    # containsprofanity - no space
    # contains profanity - has the space
    # this example no space in the url - works
    my_HTTPResponse = urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=shot")

    # broken space in url
    # space in url - contains profanity - has the space - not containsprofanity
    # urllib.error.HTTPError: HTTP Error 400: Bad Request
    # www.purgomalum.com - no auto fix
    # my_HTTPResponse = urllib.request.urlopen("http://www.purgomalum.com/service/contains profanity?text=shot")

    # normalized "broken" url
    # fixed the space note the %20 also left the back slashes alone - safe argument 
    my_quoted_fixed_url = urllib.parse.quote("http://www.purgomalum.com/service/contains profanity?text=shot", safe="%/:=&?~#+!$,;'@()*[]")
    print("my_quoted_fixed_url is %s" % my_quoted_fixed_url)
    # my_quoted_fixed_url is http://www.purgomalum.com/service/contains%20profanity?text=shot

    my_HTTPResponse.close()
    print()

    print("End url_clean_function\n")

### Begin url_clean.py module ###

print ("sys.version is %s\n" % sys.version)

url_clean_function()

#read_text()
#check_profanity(contents_of_file)

print('\nEnd url_clean module\n')

