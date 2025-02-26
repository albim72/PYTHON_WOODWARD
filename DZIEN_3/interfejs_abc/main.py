from pojazd import Pojazd

p = Pojazd()
odl = 546
jedn = 45
cenaj = 6.34
print(f'spalanie [l/100 km] -> {p.spalanie(odl,jedn)}')
print(f'koszt przejazdu na trasie {odl} km wynosi {p.koszt_przejazdu(jedn,cenaj):.2f} zł')
