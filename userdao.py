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
        
    # TODO - make id a list/tuple or a * parameter        
    #def delete_user(self, id):
    #    sql = f"DELETE FROM users WHERE id={id}"
    #    self.conn.execute(sql)
    #    self.conn.commit()

    def delete_user(self, *ids):
        if not ids:
            return

        placeholders = ",".join("?" for _ in ids)
        sql = f"DELETE FROM users WHERE id IN ({placeholders})"

        self.conn.execute(sql, ids)
        self.conn.commit()
        
    def update_user(self, user):
        sql = f"""
        UPDATE users
        SET name = '{user.name}',
            email = '{user.email}', 
            active = {1 if user.active else 0}
        WHERE id = {user.id}
        """
        self.conn.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = UserDao()
    #user = User(-1, "Yvonne", "yvonne@gmail.com", True)
    #added_user = dao.add_user(user)
    # added_user should have an id that was assigned by the db
    #print (added_user)

    dao.delete_user(1)
    dao.delete_user(1, 2, 3)
    dao.delete_user(39, 40, 41, 13)
    #dao.delete_user(37)
    #dao.delete_user(38)
    # check 34 is missing below

    users = dao.get_users()
    for user in users:
        print (user)

    #users[-1].name = "CHANGEDx"
    #users[-1].active = not users[-1].active

    #dao.update_user(users[-1])

    users = dao.get_users()
    for user in users:
        print (user)



    dao.close()



    





