from src.mini_venmo import MiniVenmo


def test_create_user():
    venmo = MiniVenmo()
    user = venmo.create_user("Alice")
    assert user.name == "Alice"
    assert str(user) == "User(name=Alice)"

    assert "Alice" in venmo.USERS
    assert venmo.USERS["Alice"] == user
