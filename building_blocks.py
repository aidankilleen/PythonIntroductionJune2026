# Building Block #1 - Comment
# comments are for humans - python interpreter (mostly) ignores them

# don't use comments to state the obvious - use comments that add value
# print "Building Blocks"

from random import randint


print ("Building Blocks")

"""
Multi line
Comment
"""

# Building Block #2
# Variable(s)
# in python there is no need to declare the variable - just use variables as you need them
name = "Aidan"

a = 10
b = 20

f = 1.23456

print (name)
# variables in python are weakly typed
# you can change the type as you code
n = 99
print (n)
n = "ninety nine" 
print (n)

# Building Block #3 
# expression - usually calculations or other operations on variables
a = 10
b = 20

answer = a + b

print (a + b)

print (a * b)
print (a / b)
print (a ** b) # to the power of
print (a - b)

# pythonic - python can natively handle really big numbers
a = 1298376419287436129876418726348912763498172634879623498612398
b = 3425908723498572348975928347509827450987234098234098707234908

print (a + b)

# pythonic - you can multiply a string
print ("*" * 50)

# python tries to be logically consistent
print (a + b)
print ("a" + "b")

# shortcut - <alt><shift><down> - copy a line
# shortcut - <alt><up> and <alt><down> move a line up  and down the file
#print ("a" * "b")
print ("a" * 50)
# shortcut - <ctrl><shift>K - delete a line

# Building Block #4
# if - conditions
# pythonic if there is a :
# the next line must be indented
# most programminglanguages ignore the whitespace
# but in python the indented blocks are part of the syntax
n = 15

if n < 10:
    print ("less than 10")
else:
    print ("greater than 10")

if n < 5:
    print ("small")
elif n < 10:
    print ("medium")
else:
    print ("large")

# you can also use a conditional expression
# inline conditional
message = "less than 10" if n < 10 else "greater than or equal to 10"


# Building Block #5
# Loops

n = 1
while n < 10:
    print(n, end=" ")
    #n = n + 1 # in python there is no n++ but you can shortcut it n += 1
    n += 1

print ()
print ("=" * 50)
# Building Block #6
# list / array
# NB: there's a bit more to this 

l = [1, 3, 5, 4, 2]

print (l[1])    #NB: list index starts at 0 [1] is the second item in the list
print (l[0])    # first item in the list
print (len(l))

# use a for loop to iterate through the items in the list
for i in l:
    print (i)

# pythonic - lists don't need to have all the items the same type
# heterogenous - the items don't need to be the same (type)
l = [3, 3.0, "three", [1,2,3]]


# Building Block #7
# functions

print (len(l))

# functions have a name
# functions may take one or more parameters
# function may return a value or answer

print (type("aidan"))
print (type(1))
print (type(1.1))


# in python we have access to the built-in functions https://docs.python.org/3/library/functions.html
# standard library function https://docs.python.org/3/library/index.html
# third party libraries https://pypi.org/
# define our own functions as well

# to use a function from the standard library you need to "import"
# from random import randint

print ("Random number:")
r = randint(1, 10)
print (r)


# define our own function
def greet(name):
    print ("Welcome " + name)


greet("Alice")
greet("Bob")
greet("Carol")
greet("Dan")


# naming convention
# use lower case

name = "Aidan"
Name = "Alice"  # it is valid to create a variable name with upper case 
                # strongly recommended not to do this

# assume that everything is case-sensitive

print (name)
print (Name)

# use _ to separate words

firstName = "Aidan" # don't use capitals to separate words
first_name = "Aidan" # use _ instead

# this is called "snake case"

# use snake_case for variables
# use snake_case for function names
# use snake_case for file names


# use all caps for constants
PI = 3.14
WEBSITE_URL = "www.professional.ie"

# NB: python doesn't prevent you from changing a constant
PI = 4


# building Block # 8 
# objects - see object_introduction.py
# use Camel case for objects
# TODO - understand objects further
# df = DataFrame()

class MyObject ():
    pass

# not:
class my_object():
    pass

class MYOBJECT():
    pass

# Really important thing to note:
# you can redefine anything and python won't complain

# print = "This is not a function"
# print ("is this working")

# be careful to not redefine core functions from python

# don't use the variable name "list" - list() is a built-in function
# list = [1, 2, 3, 4]
























































































