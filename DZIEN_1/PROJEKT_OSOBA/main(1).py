# import osoba as os
from osoba import Osoba
from pracownik import Pracownik
from student import Student

os1 = Osoba("Jan",46,102,173)
print(os1)
nlat = 8
print(f'wiek za {nlat} lat: {os1.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {os1.czypracownik()}')

print("_"*50)
os2 = Osoba("Anna",33,54,170)
os2.set_kolor_oczu("niebieskie")
print(os2)
print(f"zmieniony kolor oczu -> {os2.get_kolor_oczu()}")
nlat = 5
print(f'wiek za {nlat} lat: {os2.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {os2.czypracownik()}')

print("_"*50)
pr1 = Pracownik("Olga",40,60,173,"ABC","Dyrektor",5,10560)
print(pr1)
nlat = 3
print(f'wiek za {nlat} lat: {pr1.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {pr1.czypracownik()}')

print("_"*50)

pr2 = Pracownik("Antoni",51,78,181,"XYZ",
                "Główny Informatyk",12,9800,
                "Biegi Ultra",12,"102 km - 16h 23min 34s")
print(pr2)
nlat = 13
print(f'wiek za {nlat} lat: {pr2.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {pr2.czypracownik()}')
print(pr2.infosport())

print("_"*50)
st1 = Student("Karol",22,80,173,"Ekonomia","Makroekonomia",2)
print(st1)
nlat = 5
print(f'wiek za {nlat} lat: {st1.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {st1.czypracownik()}')

print("_"*50)
st2 = Student("Ferdynand",22,66,175,"Ekonomia","Makroekonomia",2,
              "DEREK","księgowy",2,3400)
print(st2)
nlat = 5
print(f'wiek za {nlat} lat: {st2.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {st2.czypracownik()}')

print("_"*50)
st3 = Student("Maria",23,71,179,"Automatyka i Informatyka","Informatyka",3,
              dyscyplina="pływanie",lataupr=4,bestwynik="pływanie 1500 m - 28min 12s")
print(st3)
nlat = 5
print(f'wiek za {nlat} lat: {st3.wiek_za_n_lat(nlat)}')
print(f'Czy osoba jest pracownikiem? -> {st3.czypracownik()}')
