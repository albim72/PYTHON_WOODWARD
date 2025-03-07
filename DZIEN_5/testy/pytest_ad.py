import pytest

class Database:
    def connect(self):
        return "Connected"

    def disconnect(self):
        return "Disconnected"

@pytest.fixture
def db():
    database = Database()
    yield database
    database.disconnect()

def test_db_connection(db):
    assert db.connect() == "Connected"

@pytest.fixture(params=[(2, 2, 4), (3, 3, 9), (4, 4, 16)])
def multiplication_data(request):
    return request.param

def test_multiplication(multiplication_data):
    x, y, expected = multiplication_data
    assert x * y == expected

@pytest.fixture(scope="session")
def global_resource():
    return {"data": "persistent"}

def test_global_resource(global_resource):
    assert global_resource["data"] == "persistent"

def get_username():
    return "RealUser"

def test_mocked_function(monkeypatch):
    monkeypatch.setattr("__main__.get_username", lambda: "MockedUser")
    assert get_username() == "MockedUser"

@pytest.mark.parametrize("x, y, expected", [(1, 2, 3), (4, 5, 9), (10, 15, 25)])
def test_addition(x, y, expected):
    assert x + y == expected

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
