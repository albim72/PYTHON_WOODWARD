from xyz.Colors import Colors

class MojaMeta(type):
    def __new__(cls,clsname,superclasses,attrs):
        print(f'nazwa klasy: {clsname}')
        print(f'klasy dziedziczone: {superclasses}')
        print(f'atrybuty klasy: {attrs}')
        return type.__new__(cls,clsname,superclasses,attrs)

    def one(cls):
        return 1


class S:
    pass

class F:
    pass

class Special(S,Colors,metaclass=MojaMeta):
    pass

class B(F,Special):
    def __new__(cls, *args, **kwargs):
        print("inna opcja...")
        return object.__new__(B)
    def __repr__(self):
        return "nowa reprezentacja"

class Normal:
    def msg(self,m):
        return "anb@wp.pl"

class NextC(B,Normal):
    def msg(self, m):
        return super().msg(m) + "... abc"

cf = NextC
print(cf.one())

ob = NextC()
print(ob.one())
