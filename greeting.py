# greeting.py

# module of functions for greeting

DEFAULT_GREETING="Welcome"

def greet(name="", greeting=DEFAULT_GREETING, count=1):
    for i in range(count):
        print(f"{greeting} {name}")
    

#print (f"__name__ = {__name__}")

# if this is the main module 
# run this code for testing
# if this is an imported module, don't
if __name__ == "__main__":

    # code to test the function
    greet("Alice", "Welcome", 5)
    greet("Bob", "Failte")
    greet("Carol")
    greet("Dan", count=5)


    greet(count=3, greeting="Failte", name="Eve")

    greet()