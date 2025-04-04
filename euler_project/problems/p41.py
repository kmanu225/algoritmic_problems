""" What is the largest n-digit pandigital prime that exists? """
from apremier import isprime
from apermutation import permutation, colle
import math as m


def prime_pandigital():
    e1 = permutation(["1", "2", "4", "3"])
    e2 = permutation(["1", "2", "4", "3", "5", "6", "7"])

    e1_ = []
    e2_ = []
    for i in range(len(e1)):
        if colle(e1[i]) % 2 == 1:
            e1_.append(colle(e1[i]))

    for i in range(len(e2)):
        if colle(e2[i]) % 2 == 1:
            e2_.append(colle(e2[i]))

    pandigital = e1_ + e2_
    pp = []
    cpt = 0

    for pand in pandigital:
        if isprime(pand):
            pp.append(pand)
            cpt += 1
    pp.sort()
    return cpt, pp


if __name__ == "__main__":
    print(prime_pandigital())
