import sqlite3

class Users(object):

    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.conn.execute("create table if not exists users (name text)")

    def __len__(self):
        c = self.conn.execute("select count(*) from users")
        (count,) = c.fetchone()
        return count
        # import pdb; pdb.set_trace()

    def create(self, name):
        self.name = name
        self.conn.execute("insert into users values (?)", (name,))
        self.conn.commit()
        return self
