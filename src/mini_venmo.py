from src.user import User


class MiniVenmo:
    USERS = {}

    def create_user(self, name):
        user = User(name)
        self.USERS[name] = user
        return user

    def render_feed(self):
        feed = [event
                for user in self.USERS.values()
                for event in user.retrieve_activity()]
        feed_lines = [str(event) for event in sorted(feed, key=lambda e: e.timestamp)]
        return "\n".join(feed_lines)
