from apremier import isprime
from time import time

start = time()
lim = 1000000
sup = 1000
start = time()
premiers = [p for p in range(1, lim + 1) if isprime(p)]
end = time()


def find():
    p_Max = 0
    long_Max = 0
    n = 0
    for deb in premiers[: sup + 1]:
        p_max = 0
        som = 0
        i = n
        while i < len(premiers) and som <= lim:
            som += premiers[i]

            if isprime(som) and som <= lim:
                p_max = som
                length = i - n + 1
            i += 1
        if lim >= p_max > p_Max and length > long_Max:
            p_Max = p_max
            long_Max = length
            st = premiers[i]
        n += 1

    return p_Max, long_Max, st


if __name__ == "__main__":

    print("Solution : ", find())

    print("temps d'exécution : ", end - start)
