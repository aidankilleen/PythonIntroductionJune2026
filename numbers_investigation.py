# numbers_investigation.py
# decimal
n = 10
print (n)

# binary 
n = 0b10
print (n)

# hex
n = 0x10
print (n)

# oct
n = 0o10
print (n)

n = 0b10000000

print (f"{n:0b}")
print (f"{n:0x}")
print (f"{n:0o}")

print (f"{123:0b}")


n = 0b10000000

print (f"{n:0b}")

while n > 0:
    print (f"{n:08b}")
    n >>= 1

n = int("1000", base=2)
print (n)
n = int("1000", base=8)
print (n)
n = int("1000", base=16)
print (n)

# an exception is thrown if the number is not valid
# n = int("222", base=2)

# scientific notation
n = 1.234E10
print (n)           # note that exponent numbers are floats

# complex numbers are supported too
n = 1+2j

print (n)
print (type(n))














