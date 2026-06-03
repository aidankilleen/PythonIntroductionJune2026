# set_investigation.py

# don't confuse dictionaries with sets
# they both use {}
# but they are not the same
d = {
    "name": "Alice", 
    "email": "alice@gmail.com", 
    "phone": "087 1234567"
}

print (d)
print (type(d))

# a set is a list with no duplicate items
s = {"one", "two", "three", "one", "two", "three", "four", "three", "five"}

print (s)
print (type(s))

s.add("ten")

print (s)
print (len(s))

# this is a list of sets
# not a list of dictionaries
l = [{"one", "two"}, {"two", "three"}]


# use for list comparison

colours1 = ["red", "green", "blue", "orange"]
colours2 = ["black", "white", "green", "red"]

# find the common elements
c1 = set(colours1)
c2 = set(colours2)

print (c1)
print (c2)

# intersection - items that are common
print (c1.intersection(c2))

# union - all the items no duplicates (amalgamation of the two lists)
print (c1.union(c2))

# difference
print (c1.difference(c2))
print (c2.difference(c1))

#  list comparison has many uses
# python handles this natively by having a set object


# python always tries to allow operators - If they make sense
l = [1,2,3] + [4, 5, 6]

# set operators

# & - intersection
print (c1 & c2)

# | union
print (c1 | c2)

# - difference
print (c1 - c2)
print (c2 - c1)

l = [1,1,1,1,1,2,2,2,2,3,3,3,3]
s = set(l)

print (s)































