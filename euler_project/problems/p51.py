import math
from apremier import isprime
from acombinaison import combinaisons
from time import time

start = time()


def replace(n, ndig):
    nCompatible = []
    nbreChiffres = int(math.log10(n)) + 1

    positions = combinaisons([i for i in range(nbreChiffres)], ndig)
    binPermutation = []
    for pos in positions:
        binaire = ["0"] * nbreChiffres
        for i in pos:
            binaire[i] = "1"
        binPermutation.append("".join(binaire))

    for elt in binPermutation:
        nComp = set({})
        for chiffre in range(10):
            nch = list(str(n))
            for i in range(len(elt)):
                if elt[i] == "1":
                    nch[i] = str(chiffre)
            if int("".join(nch)) >= n:
                nComp.add(int("".join(nch)))
        if n in nComp:
            l = list(nComp)
            l.sort()
            nCompatible.append(l)
    return nCompatible


def find(lim, deb=10):
    nbr = deb
    while nbr >= 0:
        if isprime(nbr):
            format = []
            for k in range(1, 1 + int(math.log10(nbr))):
                format += replace(nbr, k)

            for form in format:
                count = 0
                for elt in form:
                    if len(form) < lim:
                        break
                    if isprime(elt):
                        count += 1
                if count == lim:
                    print(form)
                    return nbr
        nbr += 1


if __name__ == "__main__":
    print("La solution est : ", find(2))
    end = time()
    print("temp d'exécution : {} secondes".format(end - start))
