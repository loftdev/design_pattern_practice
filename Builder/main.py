from build import Director, JeepBuilder, NissanBuilder

d = Director()
d.setBuilder(JeepBuilder())
d.getCar()
d.getCar().specification()

d2 = Director()
d2.setBuilder(NissanBuilder())
d2.getCar()
d2.getCar().specification()