import time
import math
import numpy as np

# ======================================================
# OPTIMIZACIÓN 1: Versión mejorada con sqrt y menos bucles
# ======================================================

def is_prime_sqrt(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return n == 2  # solo 2 es primo entre los pares

    limite = int(math.isqrt(n))  # raíz cuadrada entera

    # Recorremos solo impares hasta la raíz cuadrada
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_sqrt(limit):
    # Uso de list comprehension (más rápido que bucles normales)
    return [n for n in range(1, limit + 1) if is_prime_sqrt(n)]


# ======================================================
# OPTIMIZACIÓN 2: Sieve de Eratóstenes con NumPy (muy rápido)
# ======================================================

def sieve_numpy(limit):
    if limit < 2:
        return []

    # Creamos arreglo booleano: True = posible primo
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False  # 0 y 1 no son primos

    max_root = int(limit ** 0.5)

    # Marcamos los múltiplos como False
    for i in range(2, max_root + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = False

    # Obtenemos los índices que quedaron como True
    return np.nonzero(sieve)[0]


# ======================================================
# EJECUCIÓN DEL PROGRAMA
# Cambia una sola línea para elegir qué optimización usar
# ======================================================

if __name__ == "__main__":
    LIMIT = 100_000

    # Cambia a False para usar la optimización 1 (sqrt)
    usar_numpy = False   # True = Optimización 2, False = Optimización 1

    start = time.perf_counter()

    if usar_numpy:
        primos = sieve_numpy(LIMIT)
        print("Método utilizado: Optimización 2 (Sieve con NumPy)")
        print("Cantidad de primos:", len(primos))
    else:
        primos = find_primes_sqrt(LIMIT)
        print("Método utilizado: Optimización 1 (sqrt + mejoras)")
        print("Cantidad de primos:", len(primos))

    end = time.perf_counter()
    print(f"Tiempo total: {end - start:.6f} segundos")
