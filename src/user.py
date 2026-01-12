from src.payment import Payment

class User:
    def __init__(self, name, initial_balance=0, initial_credit=0):
        self.name = name
        self.balance = initial_balance
        self.credit = initial_credit
        self.activity = []

    def pay(self, user, amount, description=""):
        payment = Payment(amount, self, user, description=description)
        payment.process()

    def retrieve_activity(self):
        return self.activity.copy()

    def __repr__(self):
        return f"User(name={self.name})"
