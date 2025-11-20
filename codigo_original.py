# codigo_original.py
import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    # versión NO optimizada: prueba divisores desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for n in range(1, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

if __name__ == "__main__":
    LIMIT = 100_000
    start = time.perf_counter()
    primes = find_primes(LIMIT)
    end = time.perf_counter()
    print(f"Primos encontrados: {len(primes)}")
    print(f"Tiempo (s): {end - start:.6f}")
