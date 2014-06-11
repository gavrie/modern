import pytest
from modern import users

def test_add_user():
    user = users.create('danny')
    assert user.username == 'danny'

def test_retrieve_user():
    david = users.create('david')
    assert users.get('david') == david

def test_retrieve_nonexistent_user():
    with pytest.raises(LookupError):
        users.get('david')

def test_user_length():
    usernames = ['one', 'two', 'three']
    for index, username in usernames:
        assert len(users) == index
        users.create(username)

def test_delete_user():
    users.create('david')
    users.delete('david')
    assert len(users) == 0
