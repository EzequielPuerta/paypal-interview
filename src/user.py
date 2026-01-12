from src.payment import Payment

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
        if user not in self._friends:
            self._friends.append(user)
        if self not in user._friends:
            user._friends.append(self)

    @property
    def friends(self):
        return self._friends.copy()

    def __repr__(self):
        return f"User(name={self.name})"
