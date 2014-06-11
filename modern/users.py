import sqlite3

class User(object):
    def __init__(self, username):
        self.username = username
    def __eq__(self, other):
        return self.username == other.username


class Users(object):
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        c = self.conn.cursor()
        c.execute("create table if not exists users (username text unique)")

    def create(self, username):
        c = self.conn.cursor()
        c.execute("insert into users values (?)", (username,))
        return User(username)

    def delete(self, username):
        c = self.conn.cursor()
        c.execute("delete from users where username=?", (username,))

    def get(self, username):
        c = self.conn.cursor()
        c.execute("select username from users where username=?", (username,))
        result = c.fetchone()
        if not result:
            raise LookupError
        (username,) = result
        return User(username)
