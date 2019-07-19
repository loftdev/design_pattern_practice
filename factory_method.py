class PhoneCreator:
    def create(self):
        print("This is phone creator")


class Iphone(PhoneCreator):
    def build(self):
        print("new iPhone is made")


class SamsungGalaxy(PhoneCreator):
    def build(self):
        print("new Samsung Galaxy is made")


class PhoneFactory:
    @staticmethod
    def get_phone(os):
        if os == "ios":
            return Iphone().build()
        elif os == "android":
            return SamsungGalaxy().build()
        else:
            print("We are not making that phone yet")


# test code

client1 = PhoneFactory()
print("client 1")
client1.get_phone("ios")
client2 = PhoneFactory()
print("Client 2")
client2.get_phone("android")



