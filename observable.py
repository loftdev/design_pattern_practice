class Observable:
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        if not subscriber in self.subscribers:
            self.subscribers.append(subscriber)
        else:
            print("You subscribe already")

    def unregister(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
        else:
            print("You are not yet a subscriber")

    def update(self, *args, **kwargs):
        for info in self.subscribers:
            info.update(*args, **kwargs)
