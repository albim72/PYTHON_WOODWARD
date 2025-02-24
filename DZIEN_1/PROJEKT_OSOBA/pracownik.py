from osoba import Osoba
from sport import Sport
from ekstra import Ekstra

class Pracownik(Osoba,Sport,Ekstra):
    def __init__(self, imie, wiek, waga, wzrost,firma,stanowisko,lata_pracy,wynagrodzenie,
                 dyscyplina=None,lataupr=None,bestwynik=None):
        Osoba.__init__(self,imie, wiek, waga, wzrost)
        Sport.__init__(self,dyscyplina,lataupr,bestwynik)
        self.firma = firma
        self.stanowisko = stanowisko
        self.lata_pracy = lata_pracy
        self.wynagrodzenie = wynagrodzenie

    def __repr__(self):
        dane_p = (f"firma: {self.firma}\n"
                  f"stanowisko pracy: {self.stanowisko}\n"
                  f"lata pracy: {self.lata_pracy} \n"
                  f"wynagrodzenie: {self.wynagrodzenie:.2f} zł")
        if self.dyscyplina == None:
            dane_p = dane_p
        else:
            dane_p = dane_p + (f"dyscyplina: {self.dyscyplina}\n"
                               f"lata uprawiania: {self.lataupr}\n"
                               f"życiówka: {self.bestwynik}\n")
        return super().__repr__() + f"dane pracownika:\n {dane_p}"

    def czypracownik(self) -> bool:
        return True
    
    
