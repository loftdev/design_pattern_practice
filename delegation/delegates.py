class HouseBuilder:

    def build(self):
        pass


class BrickBuilder(HouseBuilder):
    def build(self):
        print("Now making the bricks")


class FoundationBuilder(HouseBuilder):
    def build(self):
        print("Constructing the foundation")