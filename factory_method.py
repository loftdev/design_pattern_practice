from abc import ABC


class PhoneCreator(ABC):

    @staticmethod
    def os_name(os):
        if os == "ios":
            return IphoneCreator().create_phone()
        elif os == "android":
            return AndroidCreator().create_phone()
        else:
            print("we are only creating ios and android phone")

    def create_phone(self):
        pass


class IphoneCreator(PhoneCreator):
    def create_phone(self):
        return IphoneBuilder().build()


class AndroidCreator(PhoneCreator):
    def create_phone(self):
        return SamsungBuilder().build()


class PhoneProduct:
    def build(self):
        pass


class IphoneBuilder(PhoneProduct):
    def build(self):
        print("New iPhone made ")


class SamsungBuilder(PhoneProduct):
    def build(self):
        print("New Samsung made")


# test code

client1 = PhoneCreator()
myphone = client1.os_name("ios")
yourphone = client1.os_name("android")
