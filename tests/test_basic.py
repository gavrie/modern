from modern.basic import add, foo

def test_basic():
    assert add(3, 4) == 7
    assert add(13, 4) == 10

def test_foo():
    assert foo() is None
