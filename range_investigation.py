# range_investigation.py

r = range(10)

for i in r:
    print (i)

for i in range(1, 5):
    print (i)

for i in range(1, 10, 2):
    print (i)

# the range (10, 1) is empty
for i in range(10, 1):
    print (i)


names = ['Alice', 'Bob', 'Carol', 'Dan']


print (names[0])
print (len(names))

# c programmers would iterate through the names
# this way
for i in range(4):
    print (names[i])

print ("*" * 50)
# but a python developer would just go
for name in names:
    print (name)















