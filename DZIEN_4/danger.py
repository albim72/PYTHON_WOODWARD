import os

mojkod = """
a=5
b=8
print(f'wynik = {a+b}')
"""

print(mojkod)
exec(mojkod)

cd = input("czy chcesz coś napisac? -> pisz tutaj ...")
exec(cd)

print('_'*50)

def calculate_per(l):
    return 4*l

def  calculate_area(l):
    return l**2

expr = input("podaj nazwę funkcji... ")

for l in range(10,50,10):
    if expr == 'calculate_per(l)':
        print(f'jeśli długośc l wynosi {l} wartośc obwodu działki to {eval(expr)} m')
    elif expr == 'calculate_area(l)':
        print(f'jeśli długośc l wynosi {l} wartośc pola działki to {eval(expr)} m2')
    else:
        print("niewłaściwa funkcja")
        break

w = input('podaj wartośc x: ')
w = eval(w)
oblicz = w*12
print(oblicz)
