class RouteFinder:
    def __init__(self):
        self.route = ""

    def calculate(self):
        pass

    def option(self):
        print(self.route)


class FastRoute(RouteFinder):
    def calculate(self):

        self.route = "This is the fastest route"


class BalanceRoute(RouteFinder):
    def calculate(self):
        self.route = "This route is the Balance route"


class LowCostRoute(RouteFinder):
    def calculate(self):
        self.route = "This is the less expensive route"
