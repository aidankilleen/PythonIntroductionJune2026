# user.py

# python module with classes for working with the users database

# User
# id
# name
# email
# active (True or False)

from random import shuffle


class User():
    def __init__(self, id, name, email, active):
        self.id = id
        self.name = name
        self.email = email
        self.active = active

    # __str__ is the string representation for the users
    def __str__(self):
        return f"{self.id}:{self.name} {self.email}{"Active" if self.active else "Inactive"}"
    
    def __repr__(self):
        #return "debug rep.."
        return self.__str__()

if __name__ == "__main__":
    u = User(1, "Alice", "alice@gmail.com", True)

    print (u)

    users = [
        User(1, "Alice", "alice@gmail.com", True), 
        User(2, "Bob", "bob@gmail.com", False), 
        User(3, "Carol", "carol@gmail.com", True), 
        User(4, "Dan", "dan@gmail.com", True), 
        User(5, "Eve", "eve@gmail.com", False)
    ]




    for user in users[::-1]:
        print (user)

    print ("*" * 50)
    active_users = [user for user in users if user.active]

    for user in active_users:
        print (user)

    print ("*" * 50)


    shuffle(users)    

    for user in users:
        print (user)

    # note - __str__ isn't being called
    print (users)





