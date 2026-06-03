# defensive_programming.py


a = 10
b = 0

if b != 0:
    answer = a / b  # program crashes here 
else:
    answer = 0


r = do_something()
if r == -1:
    print ("network error")
elif r == -2:
    print ("user error")
elif r == -3:
    print ("parameter error")
else:
    print ("everything worked")

r = do_something_else()
if r == -1:
    print ("network error")
elif r == -2:
    print ("user error")
elif r == -3:
    print ("parameter error")
else:
    print ("everything worked")

# glass is half empty approach
# constantly anticipating every possible problem
# writing lots and lots of code to handle these scenarios


print ("finished") # if there is a crash the code doesn't run to completion

