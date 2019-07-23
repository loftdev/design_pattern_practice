class CoffeeMakerMachine:
    def cost(self):
        pass


class Black(CoffeeMakerMachine):
    def cost(self):
        return 20


class CoffeeAddOn(CoffeeMakerMachine):
    def __init__(self, black):
        self.coffee = black

    def cost(self):
        pass


class Milk(CoffeeAddOn):

    def cost(self):
        return self.coffee + 5


class Sugar(CoffeeAddOn):

    def cost(self):
        return self.coffee + 5


# test code
x = Black()
xb = x.cost()
print(f"The cost of plain coffee is: {xb}")
xbm = Milk(xb).cost()
print(f"The cost of coffee if you add milk is: {xbm}")
xbms = Sugar(xbm).cost()
print(f"The cost of coffee if you add sugar is: {xbms}")
