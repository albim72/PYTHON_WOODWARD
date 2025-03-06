class Pojazd:
    def __init__(self, marka, model, maksymalna_predkosc):
        self._marka = marka
        self._model = model
        self._maksymalna_predkosc = maksymalna_predkosc

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, nowa_marka):
        if nowa_marka:
            self._marka = nowa_marka
        else:
            raise ValueError("Marka nie może być pusta")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, nowy_model):
        if nowy_model:
            self._model = nowy_model
        else:
            raise ValueError("Model nie może być pusty")

    @property
    def maksymalna_predkosc(self):
        return self._maksymalna_predkosc

    @maksymalna_predkosc.setter
    def maksymalna_predkosc(self, nowa_predkosc):
        if nowa_predkosc > 0:
            self._maksymalna_predkosc = nowa_predkosc
        else:
            raise ValueError("Maksymalna prędkość musi być większa od zera")

# Przykładowe użycie
pojazd = Pojazd("Toyota", "Corolla", 180)
print(f"Pojazd: {pojazd.marka} {pojazd.model} o maksymalnej prędkości {pojazd.maksymalna_predkosc} km/h")

# Zmiana właściwości przy użyciu setterów
pojazd.marka = "Honda"
pojazd.model = "Accord"
pojazd.maksymalna_predkosc = 200
print(f"Zaktualizowany pojazd: {pojazd.marka} {pojazd.model} o maksymalnej prędkości {pojazd.maksymalna_predkosc} km/h")
