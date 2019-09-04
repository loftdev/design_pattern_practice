import copy


class Memento:

    def __init__(self, data):
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))


class Undoable:

    def __init__(self):
        self.__last = None

    def save(self):
        self.__last = Memento(self)

    def undo(self):
        for attribute in vars(self):
            setattr(self, attribute, getattr(self.__last, attribute))


class Data(Undoable):

    def __init__(self):
        super(Data, self).__init__()
        self.numbers = []
