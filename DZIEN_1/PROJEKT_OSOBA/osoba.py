class Osoba:
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Osoba)

    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.info()

    def __repr__(self):
        return (f'reprezentacja tekstowa obiektu -> {self.imie}\n'
                f'wiek /lata/: {self.wiek}\n'
                f'wzrost /cm/: {self.wzrost}\n'
                f'waga /kg/: {self.waga}\n'
                f'kolor oczu - {self.kolor_oczu}')

    def info(self):
        print(f"Utworzono obiekt klasy: {self.__class__.__name__}")

    def wiek_za_n_lat(self,n):
        return self.wiek + n

    def czypracownik(self)->bool:
        return False
    
    def get_kolor_oczu(self):
        return self.kolor_oczu
    
    def set_kolor_oczu(self,nowy_kolor):
        self.kolor_oczu = nowy_kolor
