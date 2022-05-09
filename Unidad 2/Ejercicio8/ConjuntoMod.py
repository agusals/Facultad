class Conjunto:
    __conjunto = {}

    def __init__(self, arg: set):
        self.__conjunto = set(arg)

    def get(self):
        return self.__conjunto

    def __add__(self, otro):
        if type(self) == type(otro):
            return Conjunto(set(self.get()) | set(otro.get()))
        if type(otro) == set:
            return Conjunto(set(self.get()) | set(otro))

    def __radd__(self, otro):
        if type(self) == type(otro):
            return Conjunto(set(self.get()) | set(otro.get()))
        if type(otro) == set:
            return Conjunto(set(self.get()) | set(otro))

    def __sub__(self, otro):
        if type(self) == type(otro):
            return Conjunto(set(self.get()) - set(otro.get()))
        if type(otro) == set:
            return Conjunto(set(self.get()) - set(otro))
    
    def __rsub__(self, otro):
        if type(self) == type(otro):
            return Conjunto(set(self.get()) - set(otro.get()))
        if type(otro) == set:
            return Conjunto(set(self.get()) - set(otro))
            
    def __eq__(self, otro):
        if type(self) == type(otro):
            return self.get() == otro.get()
        if type(otro) == set:
            return self.get() == otro

    