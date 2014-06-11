from modern import users

def test_add_user():
    user = users.create('danny')
    assert user.username == 'danny'
