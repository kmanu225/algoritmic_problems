"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to lim?
"""

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


lim = 20
primes = [i for i in range(lim + 1) if isprime(i)]
power = 1

multp_min = 1

for n in primes:
    while n**power < lim:
        power += 1
    multp_min *= n ** (power - 1)
    power = 1


print(multp_min)
