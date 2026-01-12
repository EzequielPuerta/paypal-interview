from src.user import User


class MiniVenmo:
    USERS = {}

    def create_user(self, name):
        user = User(name)
        self.USERS[name] = user
        return user
