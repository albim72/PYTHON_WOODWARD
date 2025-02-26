#silnia -> n! = 1*2*3*...*n dla n>=0
#double max-> 1.8E+308
#n??? - 171
import sys
from  liczbaujemna import SilniaUjemna

sys.set_int_max_str_digits(0x10000000)
sys.setrecursionlimit(0x10000000)

def silnia(n):
    if n<0:
        raise SilniaUjemna(n)
    wynik = 1
    for i in range(1,n+1):
        wynik*=i

    return wynik

def silnia_rek(n):
    if n<0:
        raise SilniaUjemna(n)
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartosć argumentu n silnii: "))
    wynik = silnia(n)
    wynik_r = silnia_rek(n)
    print(f'silnia od n={n} wynosi {wynik}')
    print(f'silnia rekurencyjna od n={n} wynosi {wynik_r}')
    print(f'typ dla silnia -> {type(wynik)}')
    print(f'typ dla silnia rekurencyjna -> {type(wynik_r)}')
except SilniaUjemna as un:
    print(un)