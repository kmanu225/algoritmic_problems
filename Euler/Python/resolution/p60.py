from apremier import isprime
from time import time


start = time()
NbreChiffres = 4
premierInfLim = [i for i in range(10**NbreChiffres) if isprime(i)]


def concatenateIsPrime(n1, n2):
    return isprime(int(str(n1) + str(n2))) and isprime(int(str(n2) + str(n1)))


def find(l=premierInfLim):
    l.remove(2)
    l.remove(5)
    n = len(l)

    for i1 in range(n):
        for i2 in range(i1 + 1, n):
            if concatenateIsPrime(l[i1], l[i2]):
                for i3 in range(i2 + 1, n):
                    if concatenateIsPrime(l[i1], l[i3]) and concatenateIsPrime(
                        l[i3], l[i2]
                    ):
                        for i4 in range(i3 + 1, n):
                            if (
                                concatenateIsPrime(l[i1], l[i4])
                                and concatenateIsPrime(l[i4], l[i2])
                                and concatenateIsPrime(l[i3], l[i4])
                            ):
                                for i5 in range(i4 + 1, n):
                                    if (
                                        concatenateIsPrime(l[i1], l[i5])
                                        and concatenateIsPrime(l[i5], l[i2])
                                        and concatenateIsPrime(l[i3], l[i5])
                                        and concatenateIsPrime(l[i5], l[i4])
                                    ):
                                        return [l[i1], l[i2], l[i3], l[i4], l[i5]]
    return False


if __name__ == "__main__":
    sol = find()
    print(
        "Le quituplet solution est {} et la somme des nombres vaut {}.".format(
            sol, sum(sol)
        )
    )
    print("temps : ", time() - start)
