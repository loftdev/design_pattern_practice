from strategy import RouteFinder, FastRoute, BalanceRoute, LowCostRoute


class RouteFinderClient:
    def __init__(self, option: str, budget: str):
        self.option = option
        self.budget = budget
        if option == "fast" and budget == "high":
            self.routeOption = FastRoute()
        elif option == "fast" and budget == "average":
            self.routeOption = BalanceRoute()
        elif option == "fast" and budget == "low":
            self.routeOption = LowCostRoute()

    def get_route(self):
        self.routeOption.calculate()
        self.routeOption.option()
