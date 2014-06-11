class User(object):
    def __init__(self, username):
        self.username = username
    def __eq__(self, other):
        return self.username == other.username


class Users(object):
    def __init__(self):
        self.users = set()

    def create(self, username):
        self.users.add(username)
        return User(username)

    def get(self, username):
        if username in self.users:
            return User(username)
        else:
            raise LookupError
