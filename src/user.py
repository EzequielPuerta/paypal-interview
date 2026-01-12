from src.events.payment import Payment
from src.events.friend_added import FriendAdded


class User:
    def __init__(self, name, initial_balance=0, initial_credit=0):
        self.name = name
        self.balance = initial_balance
        self.credit = initial_credit
        self._activity = []
        self._friends = []

    def pay(self, user, amount, description=""):
        payment = Payment(amount, self, user, description=description)
        payment.process()

    def retrieve_activity(self):
        return self._activity.copy()

    def add_friend(self, user):
        FriendAdded(self, user).process()

    @property
    def friends(self):
        return self._friends.copy()

    def __repr__(self):
        return f"User(name={self.name})"
