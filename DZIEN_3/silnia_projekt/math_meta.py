from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'pełna nazwa metody: {func.__qualname__}')
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
        return cls

class DebugMeta(type):
    def __new__(cls,clsname,bases,attrs):
        obj = super().__new__(cls,clsname,bases,attrs)
        obj = debugmethods(obj)
        return obj

    def __init__(cls,clsname,bases,attrs):
        cls.fc = cls.fc

    def fc(cls):
        return "ważna informacja"

class Base(metaclass=DebugMeta):pass

class Calc(Base):
    def add(self,x,y):
        return (x+y)*10

    def mul(self,x,y):
        return x*y*100

    def div(self,x,y):
        return x/(y+10)

    @property
    def wart(self):
        return self.add(5,5) + self.mul(5,2)

    @property
    def stala(self):
        return 9.81

mc = Calc()
print(mc.add(4,7))
print(mc.mul(4,7))
print(mc.div(4,7))
print(mc.wart)
print(mc.fc())

df = Calc
print(df.fc())
