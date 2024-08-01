def main():
  # Setze n auf 100000
  n = 1000000
  prime_numbers = sieve_of_eratosthenes(n)
  print(prime_numbers)

def sieve_of_eratosthenes(n):
    # Initialisiere eine Liste zur Kennzeichnung von Primzahlen
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        # Wenn primes[p] nicht geändert wurde, ist sie eine Primzahl
        if primes[p]:
            # Aktualisiere alle Vielfachen von p als nicht prim
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    # Sammle alle Primzahlen
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

