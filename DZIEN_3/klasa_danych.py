from dataclasses import dataclass

class Number:
    def __init__(self,x):
        self.x=x

zb = Number(5)
print(zb.x)

print("_____ klasa danych _____")
@dataclass
class DatNumber:
    y:float
    x:int=10

    # def __init__(self,z):
    #     self.z=z


db = DatNumber(6,3)
print(db.x, db.y)

db2 = DatNumber(7)
print(db2)

class Reg:
    x:int = 1
    y:int = 4
    z:int = 8

r = Reg()
print(r.x)

print("_"*50)
@dataclass
class Dane:
    nazwa:str
    licznik:int=0
    cena:float=0.0

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self,n_1):
        self._licznik = n_1

p = Dane("pudełko",4,11.2)
print(f'produkt: {p.nazwa} -> cena {p.cena} zł -> do zapłaty: {p.cena*p.licznik} zł')

p.licznik = 16
print(f'produkt: {p.nazwa} -> cena {p.cena} zł -> do zapłaty: {p.cena*p.licznik} zł')
