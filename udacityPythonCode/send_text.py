#!/usr/bin/env python3.5

#import time
#import turtle
#import sys

import twilio
# github has the twilio code
# twilio is a folder, rest is a folder inside the twilio folder
# inside the rest folder is a __init__.py file
# TwilioRestClient is a class in the __init__.py file
from twilio.rest import TwilioRestClient

print("\nBegin\n")
print(twilio.__version__)
print()
print("twilio.__version__ is - %s\n" % twilio.__version__)
print("twilio.version is %s\n" % twilio.version)

# https://www.twilio.com/user/account/messaging/getting-started


# account_sid = "AC32a3c49700934481addd5ce1659f04d2"
account_sid = "AC28c3cf8ede2e7907f73ee038226d629e"
# account_sid = "AC636af3753d1baeebd3ed4ab4f56386d0"

#auth_token  = "{{ auth_token }}"
auth_token  = "7b136e922b8514618e546e0986da2f66"
# auth_token = "6c4ae07cdcca470866b9dc05843b2b90"

client = TwilioRestClient(account_sid, auth_token)

# message = client.messages.create(body="test", to="12026032536", from_="+12025587052") 
# message = client.messages.create(body="test", to="12026032536", from_="+15005550006") 
message = client.messages.create(body="test", to="+12026032536", from_="+13019185823") 

print (message)
print (message.sid)



print("End\n")

 
