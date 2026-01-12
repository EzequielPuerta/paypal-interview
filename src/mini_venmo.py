from src.user import User


class MiniVenmo:
    USERS = {}

    def create_user(self, name):
        user = User(name)
        self.USERS[name] = user
        return user

    def render_feed(self):
        feed_lines = [str(payment)
                      for user in self.USERS.values()
                      for payment in user.retrieve_activity()]
        return "\n".join(feed_lines)
