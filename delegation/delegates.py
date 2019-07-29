class HouseBuilderProtocol:

    def will_house_build(self):
        print("will start making house")

    def did_house_build(self):
        print("house making finished")


class BrickBuilder(HouseBuilderProtocol):

    def build(self):
        print("Now making the bricks")


class FoundationBuilder(HouseBuilderProtocol):

    def build(self):
        print("Constructing the foundation")
