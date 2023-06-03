""" Find the sum of all the primes below two million. """

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


lim = 2e6
som = 0
for n in range(int(lim)):
    if isprime(n):
        som += n

print(som)
