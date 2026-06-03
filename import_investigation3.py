# import_investigation3.py

# import the entire module and assign an alias
# use the alias when referencing or calling something
# from the module
import random as rnd

r = rnd.randint(1, 10)

print (f"r = {r}")

numbers = list(range(1, 11))

print (numbers)

rnd.shuffle(numbers)

print (numbers)

