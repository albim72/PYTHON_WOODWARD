import time
import numpy as np
from numba import jit, prange
import math
from scipy.special import gammaln

# Aproksymacja Stirlinga (zwracająca logarytm silni)
def silnia_stirling(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    return 0.5 * math.log(2 * math.pi * n) + n * (math.log(n) - 1)

# Logarytmiczne podejście do silni (bez przepełnienia)
def silnia_log(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    return gammaln(n + 1)  # Zwraca logarytm silni

# Testowanie wydajności
n = 10**15


# Pomiar czasu dla Stirlinga
start = time.time()
stirling_log = silnia_stirling(n)
stirling_time = time.time() - start

# Pomiar czasu dla logarytmicznej silni
start = time.time()
log_factorial = silnia_log(n)  # Przechowujemy log(n!)
log_time = time.time() - start

# Wyświetlenie wyników
print(f"Aproksymacja Stirlinga (log(n!)): {stirling_time:.6f} s, wynik: {stirling_log:.6f}")
print(f"Logarytm silni (gammaln): {log_time:.6f} s, wynik: {log_factorial:.6f}")