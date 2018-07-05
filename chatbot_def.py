#Yu Chang Ou | July 2018

from __future__ import unicode_literals #part of spacy
import random
import re
import string

import spacy
import en_core_web_sm
import codecs


uppercaseEntitySearch = re.compile('[A-Z]{1}[a-z]*')

responses1 = { "what is your name?" : ["My name is Echo",
                                       "They call me Echo",
                                       "I'm on an Echo, Echo, Echo"]}

responses2 = { "what's today's weather?" : "I dont know, but it might be {} today"}
weatherbank = ["sunny", "cloudy", "rainy", "hot", "cold", "humid"]


pattern = "can you help me (.*)"

responses = ["Tell me more!",
              "I dont understand",
              "Please give me something I can understand",
              "Pardon?"]


def swapPronoun(phrase):
    if 'I' in phrase:
        return re.sub('I', 'you', phrase)
    
    if 'me' in phrase:
        return re.sub('me', 'you', phrase)
    
    if 'my' in phrase:
        return re.sub('my', 'your', phrase)
    
    if 'You' in phrase:
        return re.sub('You', 'I', phrase)
    
    else:
        return phrase

def nlpVectors(message):
    nlp = spacy.load('en')
    doc = nlp(unicode(message))
    for token in doc:
        print("{} : {}".format(token, token.vector[:3]))


def respond(message):

    print uppercaseEntitySearch.findall(message)

    nlpVectors(message)
    
    if message in responses1:
        print random.choice(responses1[message])
    
    elif message in responses2:
        return responses2[message].format(random.choice(weatherbank))

    elif re.search(pattern,message):
        phrase = re.search(pattern,message).group(1)
        phrase = swapPronoun(phrase)
        return ""
        
    else:
        return random.choice(responses)
