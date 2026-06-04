# use_dao.py

from userdao import UserDao

dao = UserDao()

users = dao.get_users()

for user in users:
    print (user)

dao.close()