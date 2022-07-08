
from math import sqrt

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

primes = []
n = 2

while len(primes) != 10001:
    if isPrime(n):
        primes.append(n)
    n += 1

print("last:", primes[-1])
