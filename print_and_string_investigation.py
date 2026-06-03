# print_and_string_investigation.py


from random import randint


a = 10
b = 20
answer = a + b

# you can't add (concatenate) a number to a string 
# print ("The answer is " + answer)

# there are conversion functions (built-in)
print ("The answer is " + str(answer))

# there are lots of built-in functions for converstion 
# including int(), float(), bool(), str() and list()


# some alternatives

# print takes a variable number of parameters
print (1, 2, 3)

print ("The answer is", answer)

# there is a fature called an f-string which can do substitutions
# the expressions in the {} will be evaluated into the string
message = f"The answer is {answer}"
print (message)

print (f"{a} + {b} = {answer}")

# nb: you can put an expression into the {} it doesn't have to be a variable
print (f"{a} + {b} = {a + b}")


# you can put a conditional expression into a string:

r = randint(1, 10)

if r < 5:
    print (f"{r} is small")
else:
    print (f"{r} is large")

# do this as a single line:
print (f"{r} is {"small" if r < 5 else "large"}")

# exercise:
# do this as a single line
if r < 5:
    print (f"{r} is small")
elif r < 8:
    print (f"{r} is medium")
else:
    print (f"{r} is large")

# 
print (f"{r} is {"small" if r < 5 else "medium" if r < 8 else "large"}")


# strings we can use "", '', """"""

name = "Aidan"
name = 'Aidan'
name = """Aidan"""
name = '''Aidan'''

#use triple quotes when we need more than a single line 

a = 10
b = 20

print (f"""
    {a}
+   {b}
==========
    {a + b}
       """)

# use single quotes if you want to put in double quotes into your string
message = 'Press the "red" button'

# use double quotes if you want to put an apostrophe into your string
name = "John O'Sullivan"


# escape sequences
print ("line1\nline2\nline3\n")     # \n is a newline character

print ("col1\tcol2\tcol3")          # \t is a tab character

filepath="c:\\my documents\\newfile.txt"  # \\ puts a single \ character into your string

# \r is a carriage return
# \uXXXX is a unicode character with code XXXX

print ("\u03c0")    #π
print ("π") # you can use utf8 characters in your file anyway
print (filepath)


# formatting with widths
print (f"{a:8} + {b:8}  = {a+b:8}")

# :8 means use 8 spaces
print (f"{a:<8} + {b:>8} = {a+b:^8}")

# put in the leading zeros
print (f"""
  {a:08}
+ {b:08}
==========
  {a+b:08}

""")

name = "Aidan"
print (f"{name:*<9}")
print (f"{name:*>9}")
print (f"{name:*^9}")



# after the break - functions and function parameters



















































