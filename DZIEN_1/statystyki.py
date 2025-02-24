liczby = [877,35,2,-453,246,112,0,-9,-34,56,199,-1022,1456,89,100]

def pokaz_statystyki(dane:list)->tuple:
    minimum:float = min(dane)
    maximum:float = max(dane)
    rozstep:float = maximum - minimum
    sr_arytm: float = sum(dane)/len(dane)
    return minimum, maximum, rozstep, sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,sr = pokaz_statystyki(liczby)
print(f"wartość największa: {maxi}, najmniejsza: {mini}, rozstęp: {roz}, średnia arytmetyczna: {sr}")
