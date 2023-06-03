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


max = 0
p = None
if __name__ == "__main__":
    # for i in range(900, 1000) :
    #     if isprime(i+1) and (10**i-1)//(i+1) > max :
    #         p=1+i
    #         max = (10**i-1)//(i+1)
    i = 910
    max = (10**i - 1) // (i + 1)
    print(i, max)

    nbmax = 1000
    print([p for p in range(900, nbmax) if isprime(p)])
    # t0 = time()
    # for i in range(1000000) :
    #     isprime(i)
    # t1 = time()
    # print("dt1 : ", t1-t0)

    # for i in range(1000000) :
    #     isprimeNew(i)
    # t2 = time()

    # print("\ndt2(nouveau isprime-Tehe) : ", t2-t1)
