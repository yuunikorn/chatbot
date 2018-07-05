#Yu Chang Ou | July 2018

import random
import re
import string

from chatbot_def import *

username = str(raw_input("What is your name?: "))
Name = (username.split(" ")[-1]).strip(',.!@#$%^&*()[]{}/?<>"')
print ("Hi, " + Name + " nice to meet you!")


while (1):
    
    userAnswer = str(raw_input("ask me anything: "))
    print respond(userAnswer)
