from src.user import User


def test_user_creation():
    user = User("Alice", 100, 50)
    assert user.name == "Alice"
    assert user.balance == 100
    assert user.credit == 50


def test_user_default_values():
    user = User("Bob")
    assert user.name == "Bob"
    assert user.balance == 0
    assert user.credit == 0


def test_user_payment_with_enough_balance():
    alice = User("Alice", 100, 50)
    bob = User("Bob", 50, 25)

    alice.pay(bob, 30)
    assert alice.balance == 70
    assert alice.credit == 50

    assert bob.balance == 80
    assert bob.credit == 25


def test_user_payment_with_insufficient_balance():
    alice = User("Alice", 100, 50)
    bob = User("Bob", 50, 25)

    alice.pay(bob, 200)
    assert alice.balance == 100
    assert alice.credit == 250

    assert bob.balance == 250
    assert bob.credit == 25
