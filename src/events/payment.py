from src.events.event import Event


class Payment(Event):
    def __init__(self, amount, from_user, to_user, description):
        super().__init__()
        self.amount = amount
        self.from_user = from_user
        self.to_user = to_user
        self.description = description

    def __str__(self):
        return f"{self.from_user.name} paid {self.to_user.name} ${self.amount:.2f} for {self.description}"

    def process(self):
        if self.from_user.balance >= self.amount:
            self.from_user.balance -= self.amount
        else:
            self.from_user.credit += self.amount
        self.to_user.balance += self.amount
        self.from_user._activity.append(self)
