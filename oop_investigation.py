# oop_investigation.py


# an object is a data construct that has the data and the functions 
# grouped together in a re-usable object

#name = "Aidan"
#print(name)
#print (name.upper())


class Rectangle():

    def __init__(self, width, height):
        # __init__ is called when the object is "instantiated" (created)
        # print ("creating a Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def __str__(self):
        #return "__str__ called"
        return f"Rectangle {self.width}x{self.height} area={self.get_area()}"
    
if __name__ == "__main__":
    r = Rectangle(10, 50)
    print (r)   # print will conver this into a string

    print (f"{r.width} x {r.height}")
    print (f"Area={r.get_area()}")

    r2 = Rectangle(30, 80)
    print (f"{r2.width} x {r2.height}")
    print (f"Area={r2.get_area()}")

    print (r)
    print (r2)
