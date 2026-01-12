from src.user import User
from src.events.friend_added import FriendAdded


def test_user_creation(alice):
    user = alice
    assert user.name == "Alice"
    assert user.balance == 100
    assert user.credit == 50


def test_user_default_values():
    user = User("Bob")
    assert user.name == "Bob"
    assert user.balance == 0
    assert user.credit == 0


def test_user_payment_with_enough_balance(alice, bob):
    assert alice.balance == 100
    assert alice.credit == 50
    assert bob.balance == 50
    assert bob.credit == 25

    alice.pay(bob, 30)
    assert alice.balance == 70
    assert alice.credit == 50
    assert bob.balance == 80
    assert bob.credit == 25


def test_user_payment_with_insufficient_balance(alice, bob):
    assert alice.balance == 100
    assert alice.credit == 50
    assert bob.balance == 50
    assert bob.credit == 25

    alice.pay(bob, 200)
    assert alice.balance == 100
    assert alice.credit == 250
    assert bob.balance == 250
    assert bob.credit == 25


def test_user_retrieve_activity(alice, bob):
    alice.pay(bob, 5, description="Coffee")
    bob.pay(alice, 15, description="Lunch")

    alice_activity = alice.retrieve_activity()
    bob_activity = bob.retrieve_activity()
    assert len(alice_activity) == 1
    assert len(bob_activity) == 1

    alice_payment = alice_activity[0]
    assert alice_payment.amount == 5
    assert alice_payment.from_user == alice
    assert alice_payment.to_user == bob
    assert alice_payment.description == "Coffee"

    bob_payment = bob_activity[0]
    assert bob_payment.amount == 15
    assert bob_payment.from_user == bob
    assert bob_payment.to_user == alice
    assert bob_payment.description == "Lunch"


def test_adding_friends(alice, bob):
    assert bob not in alice.friends
    assert alice not in bob.friends
    alice.add_friend(bob)
    assert bob in alice.friends
    assert alice in bob.friends


def test_adding_friends_appears_in_retrieve_activity(alice, bob):
    assert len(alice.retrieve_activity()) == 0
    assert len(bob.retrieve_activity()) == 0
    alice.add_friend(bob)

    assert len(alice.retrieve_activity()) == 1
    assert len(bob.retrieve_activity()) == 0

    event = alice.retrieve_activity()[0]
    assert isinstance(event, FriendAdded)
    assert event.timestamp is not None
    assert event.user1 == alice
    assert event.user2 == bob
