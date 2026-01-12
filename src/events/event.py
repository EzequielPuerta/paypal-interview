from datetime import datetime, timezone


class Event:
    def __init__(self):
        self.timestamp = datetime.now(timezone.utc)
