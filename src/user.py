class User:
    def __init__(self, name, initial_balance=0, initial_credit=0):
        self.name = name
        self.balance = initial_balance
        self.credit = initial_credit

    def pay(self, user, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.credit += amount
        user.balance += amount

    def __repr__(self):
        return f"User(name={self.name})"
