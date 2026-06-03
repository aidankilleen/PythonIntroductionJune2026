# exception_investigation.py

from random import randint


a = 10
b = 0
numbers = [1, 2, 3, 4]
number = "ninety nine"
answer = 0
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
except ZeroDivisionError:
    print ("You can't divide by zero")
    answer = a
except IndexError:
    print ("Index error")
    answer = numbers[-1]
except Exception as ex:     # catch all exception handler - 
    # error handling code goes here
    print ("something went wrong")
    print (ex)
    answer = 0
finally:
    # this is code that gets run no matter what
    # if an error or if there is no error
    print (f"the answer is { answer }")

print ("finished")


