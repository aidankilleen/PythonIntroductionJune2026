# function_investigation.py

def greet(name="", greeting="Welcome", count=1):
    for i in range(count):
        print(f"{greeting} {name}")
    

greet("Alice", "Welcome", 5)
greet("Bob", "Failte")
greet("Carol")
greet("Dan", count=5)


greet(count=3, greeting="Failte", name="Eve")

greet()