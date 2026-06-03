# call_greeting.py




#from greeting import greet, DEFAULT_GREETING
from greeting import *  # not recommended!!!
greet("Zoe", "Wilkommen", 5)
print (DEFAULT_GREETING)

import greeting
greeting.greet()
print (greeting.DEFAULT_GREETING)

import greeting as gt
gt.greet()
print (gt.DEFAULT_GREETING)