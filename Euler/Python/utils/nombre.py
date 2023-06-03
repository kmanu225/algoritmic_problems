import numpy as np
import math as m

def isprime(n: int) -> bool:
    if n < 2:
        return False

    elif n == 2 or n == 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    for k in range(5, int(m.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def nb_div(n: int)->int:
    nb = 0
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0:
            nb += 2
    return nb


def div(n: int)->int:
    divisors = {1}
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors = list(divisors)
    divisors.sort()
    return divisors


cache_fib = {}
def fib(n: int) -> int:
    if n in cache_fib:
        return cache_fib[n]

    if n <= 2:
        cache_fib[n] = 1

    else:
        cache_fib[n] = fib(n - 1) + fib(n - 2)

    return cache_fib[n]


def pgcd(a: int, b: int) -> int:
    if a%b == 0:
        return b
    else :
        return pgcd(b, a%b)