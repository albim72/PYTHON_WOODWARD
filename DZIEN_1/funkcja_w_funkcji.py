#przykład 1
def witaj(imie:str) -> str:
    return f'Miło Cię widzieć {imie}'

print(witaj("Konrad"))
print(witaj(53642343))

def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu -> {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'
def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Jan"))
print(osoba(konkurs,"Anna",56,12))

#przykład 2
def rejestracja(oplata):
    def lista(nr):
        return f"jesteś na liście startowej -> nr  {nr}"
    def brak():
        return "brak wpłaty, uzupełnij!"
    def error():
        return "błąd transakcji!"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(423))
print(rejestracja(0)())
print(rejestracja(13)())

#przykład 3
def startstop(func):
    def wrapper(*args):
        print("_"*50)
        print("startowanie procesu...")
        func(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka...")

wr = startstop(zawijanie)
print(wr)
wr("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"duchanie {czego} na urodziny")

dmuchanie("świeczek")
