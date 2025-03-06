class ZbytWysokiWynikError(Exception):
    """Wyjątek podnoszony, gdy wynik jest zbyt wysoki."""
    def __init__(self, wynik):
        self.wynik = wynik
        if wynik:
            self.message = f"Wynik obliczeń jest zbyt duży: {self.wynik}"

    def __str__(self):
        print("opis usterki ->")
        if self.message:
            return self.message
        else:
            return "brak informacji"

def skomplikowane_obliczenia(a, b):
    try:
        wynik = (a ** 2 + b ** 2) / (a - b)
        if wynik > 1e6:
            raise ZbytWysokiWynikError(wynik)

    except ZeroDivisionError:
        print("Błąd: próba dzielenia przez zero")
    except ZbytWysokiWynikError as e:
        print(f"Błąd: {e}")
    except TypeError:
        print("Błąd: nieprawidłowy typ danych")
    else:
        return wynik


# Przykładowe testy funkcji
print(skomplikowane_obliczenia(5, 3))  # Obliczenie zakończone sukcesem
skomplikowane_obliczenia(3, 3)  # Wywoła ZeroDivisionError
print(skomplikowane_obliczenia(1e5, 1e3))  # Wywoła ZbytWysokiWynikError
skomplikowane_obliczenia(1e15, 1e12)  # Wywoła ZbytWysokiWynikError
skomplikowane_obliczenia("5", 2) # Wywoła TypeError
