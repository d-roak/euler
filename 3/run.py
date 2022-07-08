
from math import sqrt

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

num = 600851475143
lpf = 0

for n in range(1, int(sqrt(num))):
    if isPrime(n) and num % n == 0:
        lpf = n

print("lpf:", lpf)
