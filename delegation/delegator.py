from delegates import HouseBuilder, BrickBuilder, FoundationBuilder


class Foreman:
    def __init__(self):
        self.worker = HouseBuilder()

    def make_bricks(self):
        brick = BrickBuilder()
        brick.build()

    def build_foundation(self):
        foundation = FoundationBuilder()
        foundation.build()
