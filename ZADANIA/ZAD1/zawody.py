from abc import ABC, abstractmethod

# Klasa abstrakcyjna Zawody
class Zawody(ABC):
    def __init__(self, nazwa, dystans):
        self.nazwa = nazwa
        self.dystans = dystans

    @abstractmethod
    def opis_zawodow(self):
        pass

# Klasa UltraMaraton dziedzicząca po Zawody
class UltraMaraton(Zawody):
    def __init__(self, nazwa, dystans, przewyzszenie):
        super().__init__(nazwa, dystans)
        self.przewyzszenie = przewyzszenie

    def opis_zawodow(self):
        return f"Ultra maraton: {self.nazwa}, dystans: {self.dystans} km, przewyższenie: {self.przewyzszenie} m"

# Klasa TrailRun dziedzicząca po Zawody
class TrailRun(Zawody):
    def __init__(self, nazwa, dystans, typ_terenu):
        super().__init__(nazwa, dystans)
        self.typ_terenu = typ_terenu

    def opis_zawodow(self):
        return f"Trail run: {self.nazwa}, dystans: {self.dystans} km, typ terenu: {self.typ_terenu}"

# Klasa VerticalRun dziedzicząca po Zawody
class VerticalRun(Zawody):
    def __init__(self, nazwa, dystans, kąt_wzniesienia):
        super().__init__(nazwa, dystans)
        self.kąt_wzniesienia = kąt_wzniesienia

    def opis_zawodow(self):
        return f"Vertical run: {self.nazwa}, dystans: {self.dystans} km, kąt wzniesienia: {self.kąt_wzniesienia}°"

# Testy klas
def main():
    ultra = UltraMaraton("Ultra Górska Przygoda", 100, 4500)
    trail = TrailRun("Leśna Ścieżka", 25, "las i kamienie")
    vertical = VerticalRun("Pionowy Wyskok", 5, 30)

    zawody = [ultra, trail, vertical]

    for z in zawody:
        print(z.opis_zawodow())

if __name__ == "__main__":
    main()
