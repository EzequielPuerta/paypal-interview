from src.mini_venmo import MiniVenmo


def test_create_user():
    venmo = MiniVenmo()
    user = venmo.create_user("Alice")
    assert user.name == "Alice"
    assert str(user) == "User(name=Alice)"

    assert "Alice" in venmo.USERS
    assert venmo.USERS["Alice"] == user


def test_payments_between_users():
    venmo = MiniVenmo()
    alice = venmo.create_user("Alice")
    bob = venmo.create_user("Bob")
    charly = venmo.create_user("Charly")

    alice.pay(bob, 50)  # payment with insufficient balance
    assert alice.balance == 0
    assert alice.credit == 50
    assert bob.balance == 50
    assert bob.credit == 0

    bob.pay(charly, 30)  # payment with sufficient balance
    assert bob.balance == 20
    assert bob.credit == 0
    assert charly.balance == 30
    assert charly.credit == 0
