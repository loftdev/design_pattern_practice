from observer import Subscriber1, Subscriber2
from observable import Observable

# test code

sports_magazine = Observable()
lofty = Subscriber1()
sports_magazine.register(lofty)
mier = Subscriber2()
sports_magazine.register(mier)
sports_magazine.update("Important update", msg = "Micheal Jordan will join Lakers team")
sports_magazine.unregister(mier)
sports_magazine.update("Latest update", msg = "Mier unregistered to sports magazine")


