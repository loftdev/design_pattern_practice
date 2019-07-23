from abc import ABC


class PhoneFactory(ABC):

    @staticmethod
    def create_phone(os):
        if os == "ios":
            IphoneBuilder().build()
        elif os == "android":
            SamsungBuilder().build()
        else:
            print("we are only creating ios and android phone")


class IphoneBuilder:
    @staticmethod
    def build():
        print("New iPhone made ")


class SamsungBuilder:
    @staticmethod
    def build():
        print("New Samsung made")


# test code

client1 = PhoneFactory()
myphone = client1.create_phone("i")
yourphone = client1.create_phone("android")


