# input_investigation.py

name = input("What is your name?")

print (f"Welcome {name}")

n = input("How many times?")

if n.isnumeric():
    n = int(n)
else:
    print ("please enter a number")
    exit()




print (name * n)

n = 10

if isinstance(n, int):
    print (f"{n} is an integer")
else:
    print (f"{n} is not an integer")

n = None

if isinstance(n, int):
    print (f"{n} is an integer")
else:
    print (f"{n} is not an integer")








