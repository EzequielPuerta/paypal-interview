from src.user import User
from src.payment import Payment


def test_payment_creation():
    alice = User("Alice", 100, 50)
    bob = User("Bob", 50, 25)
    payment = Payment(from_user=alice, to_user=bob, amount=15, description="Lunch")

    assert payment.amount == 15
    assert payment.from_user == alice
    assert payment.to_user == bob
    assert payment.description == "Lunch"


def test_payment_rendering():
    alice = User("Alice", 100, 50)
    bob = User("Bob", 50, 25)

    payment = Payment(from_user=alice, to_user=bob, amount=15, description="Lunch")
    text = str(payment)
    assert text == "Alice paid Bob $15.00 for Lunch"
