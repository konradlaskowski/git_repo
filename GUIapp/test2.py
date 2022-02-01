

class Some:
    def __init__(self):
        print(self.__repr__())  # = hex(id(self))
        print(id(self))

s = Some()