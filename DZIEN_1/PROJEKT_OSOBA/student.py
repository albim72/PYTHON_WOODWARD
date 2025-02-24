from pracownik import Pracownik
from osoba import Osoba

class Student(Pracownik):
    def __init__(self, imie, wiek, waga, wzrost, wydzial, kierunek, rok_stud, firma=None, stanowisko=None,
                 lata_pracy=None, wynagrodzenie=None, dyscyplina=None,lataupr=None, bestwynik=None):
        super().__init__(imie, wiek, waga, wzrost, firma, stanowisko, lata_pracy, wynagrodzenie, dyscyplina, lataupr,
                         bestwynik)
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud

    def __repr__(self):
        nrep = Osoba.__repr__(self)

        dane_f = (f"firma: {self.firma}\n"
                  f"stanowisko pracy: {self.stanowisko}\n"
                  f"lata pracy: {self.lata_pracy} \n"
                  f"wynagrodzenie: {self.wynagrodzenie} zł\n")
        dane_s = (f"dyscyplina: {self.dyscyplina}\n"
                    f"lata uprawiania: {self.lataupr}\n"
                    f"życiówka: {self.bestwynik}\n")

        stud = (f"wydział: {self.wydzial}\n"
                f"kierunek: {self.kierunek}\n"
                f"rok studiów: {self.rok_stud}\n")


        if self.firma == None and self.dyscyplina == None:
            return nrep + stud
        elif self.firma == None:
            return nrep + stud + dane_s
        elif self.dyscyplina == None:
            return nrep + stud + dane_f
        else:
            return nrep + stud + dane_f + dane_s

    def czypracownik(self) -> bool:
        return self.firma != None



