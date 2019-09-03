from delegates import HouseBuilderProtocol, BrickBuilder, FoundationBuilder


class Foreman:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        self.worker = worker

    def make_house(self):
        self.worker.will_house_build()
        self.worker.build()
        self.worker.did_house_build()


