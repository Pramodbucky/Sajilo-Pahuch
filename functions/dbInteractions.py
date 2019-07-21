# from os import path, remove
import sqlite3
from hashlib import sha512

# if path.isfile('database.db'):
#     remove('database.db')
#
# conn = sqlite3.connect('database.db')
#
# conn.execute('CREATE TABLE clients \
#               (username TEXT, fullName TEXT, email TEXT, password TEXT, \
#               contactNo TEXT, location TEXT, citizenshipNo TEXT)')
#
# conn.close()


def addData(data):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO clients \
                    (username, fullName, email, password, \
                    contactNo, location, citizenshipNo) VALUES \
                    (?, ?, ?, ?, ?, ?, ?)', (data['username'],
                                             data['fullName'],
                                             data['email'],
                                             sha512(
            data['password'].encode()
        ).hexdigest(),
            data['contactNo'],
            data['location'],
            data['citizenshipNo']))
        conn.commit()
    conn.close()


def vaildateCreds(data):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        resz = cur.execute('SELECT username, password FROM clients').fetchall()
        if not resz:
            return False
        for res in resz:
            print(res)
            if data['username'] == res[0]:
                if sha512(data['password'].encode()).hexdigest() == res[1]:
                    return True
    conn.close()
    return False
