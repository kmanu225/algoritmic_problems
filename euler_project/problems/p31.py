"""On peut écrire montant = 1a + 2b + 5c + 10d + 20e + 50f + 100g + 200h"""
from functools import lru_cache
import math
from time import time

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

start = time()


def montantComb1(m):
    if 0 < m <= 2:
        return m

    count = 0
    if m in pieces:
        count = 1
    for a in range(m // pieces[0] + 1):
        for b in range(m // pieces[1] + 1):
            if a + 2 * b < m:
                for c in range(m // pieces[2] + 1):
                    if 1 * a + 2 * b + 5 * c < m:
                        for d in range(m // pieces[3] + 1):
                            if 1 * a + 2 * b + 5 * c + 10 * d < m:
                                for e in range(m // pieces[4] + 1):
                                    if 1 * a + 2 * b + 5 * c + 10 * d + 20 * e < m:
                                        for f in range(m // pieces[5] + 1):
                                            if (
                                                1 * a
                                                + 2 * b
                                                + 5 * c
                                                + 10 * d
                                                + 20 * e
                                                + 50 * f
                                                < m
                                            ):
                                                for g in range(m // pieces[6] + 1):
                                                    if (
                                                        1 * a
                                                        + 2 * b
                                                        + 5 * c
                                                        + 10 * d
                                                        + 20 * e
                                                        + 50 * f
                                                        + 100 * g
                                                        + 200
                                                        == m
                                                    ):
                                                        count += 1
                                                    elif (
                                                        1 * a
                                                        + 2 * b
                                                        + 5 * c
                                                        + 10 * d
                                                        + 20 * e
                                                        + 50 * f
                                                        + 100 * g
                                                        == m
                                                    ):
                                                        count += 1

                                            elif (
                                                1 * a
                                                + 2 * b
                                                + 5 * c
                                                + 10 * d
                                                + 20 * e
                                                + 50 * f
                                                == m
                                            ):
                                                count += 1

                                    elif 1 * a + 2 * b + 5 * c + 10 * d + 20 * e == m:
                                        count += 1

                            elif 1 * a + 2 * b + 5 * c + 10 * d == m:
                                count += 1

                    elif 1 * a + 2 * b + 5 * c == m:
                        count += 1

            elif 1 * a + 2 * b == m:
                count += 1
    return count


@lru_cache
def montantComb2(target, avc):
    if avc <= 0:
        return 1

    res = 0
    while target >= 0:
        res = res + montantComb2(target, avc - 1)
        target = target - pieces[avc]
    return res


if __name__ == "__main__":
    m = 200
    # print("Nombre de possibilités(1) : ", montantComb1(n))
    print("Nombre de possibilités(2) : ", montantComb2(m, 7))
    print("temps d'exécution : ", time() - start)
