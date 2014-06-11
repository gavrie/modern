from modern.greet import greet

def test_greet_moshe():
    assert greet("Moshe") == "Hello Moshe"

def test_greet_ruby():
    assert greet("Ruby") == "Hello Ruby"
