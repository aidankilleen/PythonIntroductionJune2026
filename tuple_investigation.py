# tuple_investigation.py

l = [1, 2, 3, 4]    # this is a list

t = (1, 2, 3, 4, 5, 6, 7, 8)    # this is a tuple

print (t)

print (len(t))

print (t[0])
print (t[-1])

print (t[2:5])

print (t[:4])
print (t[4:])

print (t[::2])
print (t[::-1])

# t[0] = 999

# tuples are read-only list
# tuples are immutable list

# why is python keen on immutable things?
# immutable things can be optimised because they won't grow or shrink
# if something is immutable it can't be inadertently changed
# software engineers are very keen on having things that can't be changed
# because it eliminates a lot of potential bug


# uses for tuples

# use 1 - returning multiple results from a function

def process_list(numbers):

    mx = max(numbers)
    mn = min(numbers)

    return (mx, mn)

numbers = [1, 99, 108, 77, 65, 34, 29]
result = process_list(numbers)
print (result)

# use 2 -  multiple assignments
(a, b, c, d) = (1, 2, 3, 4)
print (a, b, c, d)

(max_val, min_val) = process_list(numbers)

print (max_val, min_val)

# use 3 - swap two variables - without using a temporary variable
a = 10
b = 20

print (f"{a} {b}")
# traditional way using a temporary variable
t = a
a = b
b = t

print (f"{a} {b}")

(a, b) = (b, a)

print (f"{a} {b}")


# you can modify a tuple by converting it to a list
t = (1, 2, 3)
print(t)

l = list(t)

l[0] = 999

t = tuple(l)

print (t)

# you can create a tuple with a single item
t = (1)

print (t) # not a tuple

t = (1,)
print (t) # is a tuple


# you can sometimes leave out the () when working with tuples

a, b, c, d = 1, 2, 3, 4
mxv, mnv = process_list(numbers)
a, b = b, a


t = (1, 2, 3)
a, b, c = t
print (a, b, c)


l = [1, 2, 3]
a, b, c = l
print (a, b, c)


# two places where we will encounter tuples:

d = {
    "name":"Alice", 
    "email":"alice@gmail.com", 
    "phone":"087 1234567"
}


print (d.keys())
print (d.values())

print(d.items())    #d.items() returns a list of tuples

for item in d.items():
    print (f"{item[0]} - {item[1]}")

# use a tuple to extract the two pieces
for (key, value) in d.items():
    print (f"{key} - {value}")

# a lot of python developers would leave out the ()
for key, value in d.items():
    print (f"{key} - {value}")


print ("*" * 50)
# enumerate() function

names = ["Alice", "Bob", "Carol", "Dan", "Eve"]

#non pythonic way
n = 1
for name in names:
    print (f"{ n } {name}")
    n += 1

# pythonic way is to use the enumerate function
for index, item in enumerate(names, 1):
    print (f"{index} {item}")


# C# added support for tuples relatively recently
# tuples were a core python feature from day 1 (1993)



# extraction and assignment features work with a list as well

l = [1, 2, 3]

[a, b, c] = l

print (a, b, c)


l = [(1, "Alice"), 
     (2, "Bob"), 
     (3, "Carol")
     ]

for id, name in l:
    print (id, name)

# this works in a list comprehension
labels = [f"{id}:{name}" for id, name in l]

print (labels)





















































































