# list_comprehension_investigation.py

names = ["alice", "bob", "carol", "dan", "eve"]

capitalised_names = []

for name in names:
    capitalised_names.append(name.capitalize())

print (names)
print (capitalised_names)

# this common operation - taking one list and creating another 
# has a python shortcut - list comprehension

# use a list comprehension for this style of "map" operation
capitalised_names = [name.capitalize() for name in names]

print (names)
print (capitalised_names)


# use a list comprehension to filter a list
numbers = list(range(1, 11))

odd_numbers = [n for n in numbers if n % 2 == 1]

print (numbers)
print (odd_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print (even_numbers)

# use a list comprehension to combine two lists
colours = ["red", "green", "blue"]
products = ["pen", "pencil", "crayon"]

product_list = [f"{colour} {product}"  for product in products for colour in colours ]
print (product_list)

product_list = [f"{colour} {product}"  for colour in colours for product in products ]
print (product_list)


# use this feature to create a full deck of playing cards
# suits -  hearts, spades, diamonds, clubs
# values = A, 2, 3, 4, 5..., 10, J, Q, K
# Can you use a list comprehension to create a full deck
# ["AH", "2H", ..., "KC"... "KD"]

suits=["H", "S", "D", "C"]
numbers = list(range(2, 11))
values = ["A", numbers, "J", "Q", "K"]
print (values)

values=["A"] + list(range(2, 11)) + ["J", "Q", "K"]

print (suits)
print (values)

cards = [f"{value}{suit}" for suit in suits for value in values]

print (cards)

from random import shuffle

shuffle(cards)


print (cards)



























