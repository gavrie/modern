import mock
import pytest
import modern.users

sqlite3 = mock.MagicMock()


@pytest.fixture
def users():
    modern.users.sqlite3 = sqlite3
    return modern.users.Users()

def test_add_user(users):
    user = users.create('danny')
    assert user.username == 'danny'

def test_retrieve_user(users):
    # import pdb; pdb.set_trace()
    cursor = sqlite3.connect().cursor()
    assert cursor.execute.call_count == 1
    david = users.create('david')
    assert cursor.execute.call_count == 2
    cursor.fetchone.return_value = ('david',)
    assert users.get('david') == david
    assert cursor.execute.call_count == 3

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

