from src.events.event import Event


class FriendAdded(Event):
    def __init__(self, user1, user2):
        super().__init__()
        self.user1 = user1
        self.user2 = user2

    def __str__(self):
        return f"{self.user1.name} added {self.user2.name} as a friend"

    def process(self):
        if self.user2 not in self.user1._friends:
            self.user1._friends.append(self.user2)
            self.user1._activity.append(self)
        if self.user1 not in self.user2._friends:
            self.user2._friends.append(self.user1)
