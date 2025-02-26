import time
import numpy as np
from numba import jit, prange

# Definicja funkcji na CPU
def silnia_iter(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

# Optymalizacja z Numba dla dużych n
@jit(nopython=True, parallel=True)
def silnia_numba(n):
    wynik = 1
    for i in prange(1, n + 1):
        wynik *= i
    return wynik

# Optymalizacja z Numpy dla dużych n
def silnia_numpy(n):
    return np.prod(np.arange(1, n + 1, dtype=np.float64))

# Testowanie wydajności
n = 1000000000

# Pomiar czasu CPU (Numpy)
start = time.time()
silnia_numpy(n)
cpu_time_numpy = time.time() - start

# Kompilacja JIT i pomiar czasu GPU
start = time.time()
silnia_numba(n)
gpu_time_numba = time.time() - start

# Wyświetlenie wyników
print(f"Iteracyjna na Numpy: {cpu_time_numpy:.6f} s")
print(f"Iteracyjna na Numba (GPU optymalizacja): {gpu_time_numba:.6f} s")
