from observer.observer import Observable
from observer.observer import Subscriber1, Subscriber2

# test code

sports_magazine = Observable()
lofty = Subscriber1()
sports_magazine.register(lofty)
mier = Subscriber2()
sports_magazine.register(mier)
sports_magazine.update("Important update", msg = "Micheal Jordan will join Lakers team")


