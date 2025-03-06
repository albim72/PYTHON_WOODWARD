from zawody import *
from decor import *

# Test dekoratora
print(obliczenia_m(5, 3))  # Wynik: 15, ponieważ wybrano operację 'mnożenie'
print(obliczenia_d(4,3))
print(obliczenia_d(4,0))

def main():
    ultra = UltraMaraton("Ultra Górska Przygoda", 100, 4500)
    trail = TrailRun("Leśna Ścieżka", 25, "las i kamienie")
    vertical = VerticalRun("Pionowy Wyskok", 5, 30)

    zawody = [ultra, trail, vertical]

    for z in zawody:
        print(z.opis_zawodow())

if __name__ == "__main__":
    main()
