# import_investigation.py

from random import randint, shuffle

r = randint(1, 10)

print (f"r = {r}")

numbers = list(range(1, 11))

print (numbers)

shuffle(numbers)

print (numbers)