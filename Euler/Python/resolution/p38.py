import math as m
from time import time

chiffres = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def ispandigital(l, data=chiffres):
    conc = []
    for elt in l:
        conc += list(str(elt))
    conc.sort()
    return conc == chiffres


def concatenate(l):
    conc = ""
    for elt in l:
        conc += str(elt)
    return int(conc)


def find():
    ensemble = []
    maxi = 10000
    m = [i for i in range(1, 10)]
    produit = []

    for m1 in range(1, maxi + 1):
        for i in range(10):
            produit.append(m[i] * m1)
            if ispandigital(produit) or concatenate(produit) > 9876543211:
                if ispandigital(produit):
                    ensemble.append([m1, m[: i + 1], concatenate(produit)])
                break
        produit = []
    ensemble.sort()
    return ensemble


# print(ispandigital([192, 384, 576]))
# print(concatenate([192, 384, 576]))

deb = time()
print("solutions :\n{} \n".format(find()))
print("\ntemps = ", time() - deb)
