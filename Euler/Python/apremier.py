import math as m
from time import time


def prime(n):
    if n == 1:
        return False

    if n == 2:
        return True

    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def isprimeNew(n):
    if n <= 1:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False

    else:
        i = 5
        while i <= m.ceil(m.sqrt(n)):
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
            i += 6
        return True


def isprime(n):
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




if __name__ == "__main__":
    nbmax = 1000
    print([p for p in range(nbmax) if isprime(p)])
