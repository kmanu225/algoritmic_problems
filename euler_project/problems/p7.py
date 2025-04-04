""" What is the lim-st prime number? """

import math as m


def isprime(n):
    if n == 2:
        return True

    elif n < 2:
        return False

    else:
        for d in range(2, m.floor(m.sqrt(n)) + 1):
            if n % d == 0:
                return False

    return True


lim = 10001
count = 0
nombre = 0
prime = None
while count < lim:
    if isprime(nombre):
        prime = nombre
        count += 1
    nombre += 1
print(prime)
