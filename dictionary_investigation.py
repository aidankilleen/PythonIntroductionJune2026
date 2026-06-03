# dictionary_investigation.py


d = {
    "name":"Alice", 
    "email":"alice@gmail.com", 
    "phone":"087 1234567"
}

print (d)

print (d["name"])
print (d["phone"])

keys = d.keys()

print (keys)
print (d.values())

# python is logically consistent
names=["Alice", "Bob", "Carol"]

# if you can iterate through the items in a list
for name in names:
    print (name)

# can you iterate through the keys in a dictionary - yes!!!
for key in d:
    print (f"{key}:{d[key]}")


# you can add an item to a dictionary
d["department"] = "sales"

print (d)

# you can modify an item in a dictionary
d["name"] = "Alicia"

print (d)

# you can remove an item from a dictionary
del d["name"]

print (d)

# we're going to see dictionaries in all sorts of places
# over the next 3 days




















