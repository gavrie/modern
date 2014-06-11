import pytest
import modern.users

@pytest.fixture
def users():
    return modern.users.Users()

def test_add_user(users):
    user = users.create('danny')
    assert user.username == 'danny'

def test_retrieve_user(users):
    david = users.create('david')
    assert users.get('david') == david

def test_retrieve_nonexistent_user(users):
    with pytest.raises(LookupError):
        users.get('david')

def test_delete_user(users):
    users.create('david')
    users.delete('david')
    with pytest.raises(LookupError):
        users.get('david')

# def test_user_length():
#     usernames = ['one', 'two', 'three']
#     for index, username in usernames:
#         assert len(users) == index
#         users.create(username)

