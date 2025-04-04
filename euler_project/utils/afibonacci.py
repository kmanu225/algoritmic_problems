from functools import lru_cache
from time import time


def fib1(n):
    if n <= 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


cache_fib = {}
def fib2(n):
    if n in cache_fib:
        return cache_fib[n]

    if n <= 2:
        cache_fib[n] = 1

    else:
        cache_fib[n] = fib2(n - 1) + fib2(n - 2)

    return cache_fib[n]


@lru_cache
def fib3(n):
    if n <= 2:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2)


if __name__ == "__main__":
    t0 = time()
    for i in range(1, 30):
        fib1(i)
        # print(i, ":", fib1(i))

    t1 = time()
    for i in range(1, 20002):
        fib2(i)
        # print(i, ":", fib2(i))

    t2 = time()
    for i in range(1, 20002):
        fib3(i)
        # print(i, ":", fib3(i))
    t3 = time()

    print("dt1", t1 - t0)
    print()
    print("dt2", t2 - t1)
    print()
    print("dt3", t3 - t2)
