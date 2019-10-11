from builder import JeepBuilder, Director, Car
from prototype import Point

d = Director()
d.setBuilder(JeepBuilder())
jeep = d.getCar()
jeep.specification()

jeep2 = jeep.clone()
jeep2.specification()

pO = Point(0, 0)
print(pO.__str__())
p1 = pO.clone(1, 1)
print(p1.__str__())

