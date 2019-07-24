class Observer:
    def update(self, *args, **kwargs):
        pass


class Subscriber1(Observer):
    def update(self, *args, **kwargs):
        print("Good day this is the latest news: {0}\n{1}".format(args, kwargs))


class Subscriber2(Observer):
    def update(self, *args, **kwargs):
        print("Today's update: {0}\n{1}".format(args, kwargs))
