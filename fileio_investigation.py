# fileio_investigation.py

# read a file
fs = open("testfile.txt")
lines = fs.readlines()
print (lines)
fs.close()


# write a file
names = ['Alice', 'Bob', 'Carol', 'Dan', 'Eve']

fs = open("names.txt", "w")

for name in names:
    fs.write(f"{name}\n")

fs.close()


# you can use "with" to automatically close your
# files

with open("names.txt") as fi:
    names = fi.readlines()

# fi is automatically closed at the end of with

with open ("copy.txt", "w") as fo:

    for name in names:
        fo.write(name)

# fo is automatically closed at the end of with
















