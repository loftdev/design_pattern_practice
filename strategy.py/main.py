from strategyClient import RouteFinderClient

"""
For test purpose only first parameter input is "fast",     
second parameter input is "high, average and low"
"""

lofty = RouteFinderClient("fast", "high")
lofty.get_route()

mier = RouteFinderClient("fast", "low")
mier.get_route()

me = RouteFinderClient("fast", "average")
me.get_route()
