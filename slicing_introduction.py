# slicing_introduction.py

numbers = [6, 5, 3, 1, 2, 9, 10, 8, 7, 4, 15, 12, 13, 11]

print (numbers)
print (len(numbers))

print (numbers[0])  # first item in list

# pythonic feature - you can use a negative index!

print (numbers[-1]) # last item in the list


# slicing - pythonic [start:stop:step]
print (numbers[5:10])   # start:stop   - start inclusive, stop is exclusive

# this is logically consistent with the range(start, stop) start inclusive, stop exclusive

print (numbers[:10]) # leave out the start it will default to 0
print (numbers[10:]) # leave out the stop it will default to the end


# start:stop:step
print (numbers[1:10:2])

numbers = list(range(1, 11))
print (numbers)
print (numbers[::2])    # every second item starting at 0
print (numbers[1::2])   # every second item starting at 1

# negative step means go backwards i.e. reversed
print (numbers[::-1])


# is this consistent???
# exercise - do these slicing operations work on a string?

s = "abcdefghijklmnopqrstuvwxyz"

print(s)
print (s[0])
print (len(s))

# exercise:
# do the other slicing operations work?
# (5 minutes)

print (s[-1])

print (s[5:10])

print (s[:10])
print (s[10:])

print (s[::2])
print (s[1::2])

print (s[::-1])


# string operations

s1 = s[::2]
s2 = s[1::2]

# you can add two string
s = s1 + s2
print (s)

# you can multiply a string by an integer
s = "abc" * 5

print (s)

# what about a list
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# you can add two lists together
print (l1 + l2)

# you can multiply a list by an integer
print (l1 * 5)



































