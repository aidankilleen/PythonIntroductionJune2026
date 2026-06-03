# exception_investigation.py

from random import randint


a = 10
b = 0
numbers = [1, 2, 3, 4]
number = "ninety nine"

r = randint(1, 4)
try:
    if r == 1:
        answer = int(number)
    elif r == 2:
        answer = numbers[4]
    elif r == 3:
        answer = a / b
    else:
        answer = 42     # no error 
except:
    # error handling code goes here
    print ("something went wrong")
    answer = 0

print (f"the answer is { answer }")
print ("finished")


