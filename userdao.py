# userdao.py

# Data Access Object for reading and writing users to and from the db

import sqlite3

from user import User


class UserDao():
    def __init__(self):
        self.filename = "users.db"
        self.conn = sqlite3.connect(self.filename)

    def get_users(self):
        sql = "SELECT * FROM users"
        cur = self.conn.execute(sql)
        users = []
        for id, name, email, active in cur:
            user = User(id, name, email, active)
            users.append(user)
        return users

    def add_user(self, user):
        sql = f"""
        INSERT INTO users 
        (name, email, active) 
        VALUES('{user.name}', '{user.email}', {1 if user.active else 0})
        """
        cur = self.conn.execute(sql)
        self.conn.commit()
        user.id = cur.lastrowid
        return user
        
    def delete_user(self):
        pass
    def update_user(self):
        pass
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = UserDao()
    user = User(-1, "Yvonne", "yvonne@gmail.com", True)
    added_user = dao.add_user(user)
    # added_user should have an id that was assigned by the db
    print (added_user)


    users = dao.get_users()
    for user in users:
        print (user)

    dao.close()



    





