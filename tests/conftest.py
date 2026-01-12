from pytest import fixture
from src.user import User


@fixture
def alice():
    return User("Alice", 100, 50)

@fixture
def bob():
    return User("Bob", 50, 25)

@fixture
def charly():
    return User("Charly", 75, 30)
