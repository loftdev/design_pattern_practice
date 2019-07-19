class Singleton:
    _instance = None

    def __new__(cls, val=None):

        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)
        Singleton._instance.val = val
        return Singleton._instance


# test code

user1 = Singleton()
user1.val = "chicken"
print("the value of user1 is " + user1.val)
user2 = Singleton()
user2.val = "Pig"
print("The value of user2 is " + user2.val)
print("The value of user1 now is " + user1.val)
print("if user1 is the same with user2, Singleton works")
