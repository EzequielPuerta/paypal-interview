class Payment:
    def __init__(self, amount, from_user, to_user, description=""):
        self.amount = amount
        self.from_user = from_user
        self.to_user = to_user
        self.description = description

    def process(self):
        if self.from_user.balance >= self.amount:
            self.from_user.balance -= self.amount
        else:
            self.from_user.credit += self.amount
        self.to_user.balance += self.amount
        self.from_user.activity.append(self)
