def logger(self,m,n):
    return f"{m}:{n}"

class MultiBases(type):
    def __new__(cls,clsname,bases,attrs):
        if len(bases)>1:
            raise TypeError("Wielodziedziczenie jest zabronione!")
        return type.__new__(cls,clsname,bases,attrs)

    def __init__(self, clsname, bases, attrs):
        self.logger = logger


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class Ekstra:
    pass

class B(A):
    pass

b = B()
print(f'{b.logger(34,"info")}')

def policz(self,x,y):
    return x*y-10

B.logger = policz
c = B()
print(c.logger(27,78))

a = A()
print(a.logger(45,6))



