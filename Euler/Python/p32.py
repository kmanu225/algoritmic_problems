""" Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital. """
import math as m
from time import time
from apermutation import colle, permutation2, size

chiffres = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutations = permutation2(0)


def nuplet(n):
    e = list(permutations)
    for i in range(len(e)):
        e[i] = colle(permutations[i][:n])
    e.sort()

    uplet = []
    i = 0
    while i < len(e):
        uplet.append(e[i])
        i += m.factorial(size - n)
    return uplet


def ispandigital(m1, m2, p, data=chiffres):
    l = list(str(m1)) + list(str(m2)) + list(str(p))
    l.sort()
    return l == data


def find():
    # uplet5 = nuplet(chiffres, 5)
    uplet4 = nuplet(4)
    uplet3 = nuplet(3)
    uplet2 = nuplet(2)
    uplet1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    i = 0
    ensemble = {}
    for m1 in uplet3:
        for m2 in uplet2:
            if m1 * m2 in uplet4 and ispandigital(m1, m2, m1 * m2):
                i += 1
                ensemble[i] = [m1, m2, m1 * m2]

    for m1 in uplet1:
        for m2 in uplet4:
            if m1 * m2 in uplet4 and ispandigital(m1, m2, m1 * m2):
                i += 1
                ensemble[i] = [m1, m2, m1 * m2]

    return ensemble


# Mission


if __name__ == "__main__":
    deb = time()
    sol = find()
    som = 0
    for val in sol.values():
        som += val[2]
    fin = time()

    print(
        "solutions : \n{}\n somme = {}\n temps = {}".format(
            sol, som - 5346 - 5796, fin - deb
        )
    )


# print("pour 5 :\n{}\n on a en tous {}éléments\n\n ".format(uplet5, len(uplet5)))
# print("pour 4 :\n{}\n on a en tous {}éléments\n\n ".format(uplet4, len(uplet4)))
# print("pour 3 :\n{}\n on a en tous {}éléments\n\n ".format(uplet3, len(uplet3)))
# print("pour 2 :\n{}\n on a en tous {}éléments\n\n ".format(uplet2, len(uplet2)))
# print("pour 1 :\n{}\n on a en tous {}éléments\n\n ".format(uplet1, len(uplet1)))
