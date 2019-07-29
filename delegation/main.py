from delegator import Foreman
from delegates import HouseBuilderProtocol, BrickBuilder, FoundationBuilder


# test the code

delegate = BrickBuilder()
foreman = Foreman()
foreman.set_worker(delegate)
foreman.make_house()
delegate = FoundationBuilder()
foreman.set_worker(delegate)
foreman.make_house()



"""
foreman = Foreman()
print("foreman now exist")
print("foreman wants to build the foundation")
foreman.build_foundation()
print("The foreman wants to make the bricks")
foreman.make_bricks()
"""

