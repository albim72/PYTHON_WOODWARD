import time
from numba import jit
import sys
sys.set_int_max_str_digits(0x10000000)
sys.setrecursionlimit(0x10000000)
# Definicja funkcji na CPU
def silnia(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    if n == 0:
        return 1
    else:
        return n * silnia_rek(n - 1)

# Funkcje zoptymalizowane dla GPU
@jit(nopython=True)
def silnia_gpu(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

@jit(nopython=True)
def silnia_rek_gpu(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    if n == 0:
        return 1
    else:
        return n * silnia_rek_gpu(n - 1)

# Testowanie wydajności
n = 5000

# Pomiar czasu CPU
start = time.time()
silnia(n)
cpu_time_iter = time.time() - start

start = time.time()
silnia_rek(n)
cpu_time_rek = time.time() - start

# Kompilacja JIT i pomiar czasu GPU
start = time.time()
silnia_gpu(n)
gpu_time_iter = time.time() - start

start = time.time()
silnia_rek_gpu(n)
gpu_time_rek = time.time() - start

# Wyświetlenie wyników
print(f"Iteracyjna na CPU: {cpu_time_iter:.6f} s")
print(f"Rekurencyjna na CPU: {cpu_time_rek:.6f} s")
print(f"Iteracyjna na GPU (Numba JIT): {gpu_time_iter:.6f} s")
print(f"Rekurencyjna na GPU (Numba JIT): {gpu_time_rek:.6f} s")
