import mock
import modern.users
modern.users.sqlite3 = mock.MagicMock()

def test_create_user():
    users = modern.users.Users()
    assert users.conn.execute.called #assert_called_with('create table if not exists users (name text)')
    args, kwargs = users.conn.execute.call_args
    assert 'create table' in args[0]

    moshe = users.create("moshe")
    # users.conn.execute.assert_called_with(2)
    assert moshe.name == "moshe"
