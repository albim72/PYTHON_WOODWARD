from functools import wraps

# Dekorator pozwalający na wybór operacji
def wybierz_operacje(operacja):
    def dekorator(funkcja):
        @wraps(funkcja)
        def opakowanie(*args, **kwargs):
            if operacja == 'dodawanie':
                return args[0] + args[1]
            elif operacja == 'odejmowanie':
                return args[0] - args[1]
            elif operacja == 'mnożenie':
                return args[0] * args[1]
            elif operacja == 'dzielenie':
                if args[1] == 0:
                    return "Błąd: dzielenie przez zero"
                return args[0] / args[1]
            else:
                return "Nieznana operacja"
        return opakowanie
    return dekorator

# Przykładowa funkcja testowa
@wybierz_operacje('mnożenie')
def obliczenia_m(a, b):
    pass  # Funkcja nie musi nic robić, dekorator przejmuje działanie

@wybierz_operacje('dzielenie')
def obliczenia_d(a, b):
    pass  # Funkcja nie musi nic robić, dekorator przejmuje działanie


