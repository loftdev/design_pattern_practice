from abc import ABC


class PhoneFactory(ABC):
    def __init__(self, os):
        self.os = os

    def build(self):

        if self.os == "ios":
            IphoneBuilder(self.os).build()
        elif self.os == "android":
            SamsungBuilder(self.os).build()
        else:
            print("We are not yet creating that phone")


class IphoneBuilder(PhoneFactory):
    def build(self):
        print("New iPhone made ")


class SamsungBuilder(PhoneFactory):
    def build(self):
        print("New Samsung made")


# test code

client1 = PhoneFactory("ios")
print(client1.build())
client2 = PhoneFactory("android")
print(client2.build())