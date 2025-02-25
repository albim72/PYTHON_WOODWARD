from abc import ABC, abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,m):
        return f"metoda nieabstrakcyjna: {m}"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*5


class Regular(Prototyp):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1099

    def policz_x(self):
        return super().policz_x() + self.y*2


r = Regular(5,3)
print(r.policz())
print(r.policz_x())
