# db_investigation.py
import sqlite3

filename = "users.db"
conn = sqlite3.connect(filename)

# the database uses commands that are written in "SQL"
# Structured Query Language

# create the SQL for the query


# send the sql to the database
# database will run the SQL
# and return the results

# CRUD
# Create
# Retrieve
# Update
# Delete

# if you do these 4 operations you can work with databases
# (as a programmer)

sql = "UPDATE users SET name='Changedxxxxx' WHERE id = 11"
conn.execute(sql)
conn.commit()


sql = "INSERT INTO users (name, email, active) VALUES('Zoe', 'zoe@gmail.com',0)"
cur = conn.execute(sql)
conn.commit()

print (cur.lastrowid)


sql = "SELECT * FROM users"
cur = conn.execute(sql)

for (id, name, email, active) in cur:
    print (f"{id:10} {name:20}{email:20}{"Active" if active else "Inactive"}")

sql = "DELETE FROM users WHERE name = 'Zoe'"
cur = conn.execute(sql)
conn.commit()

conn.close()


