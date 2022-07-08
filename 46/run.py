from math import sqrt

comp  = []
prime = []

for n in range(2, 10000):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0: comp.append(n)
            break
    if n not in comp:
        prime.append(n)
    elif n % 2 != 0:
        found = False
        for i in prime:
            for j in range(10000):
                if n == i + (2 * (j ** 2)):
                    found = True
                    break
                elif n < i + (2 * (j ** 2)):
                    break
            if found:
                break
        if not found:
            print("found:", n)
            break

