from time import time


def sousEnsembles2(ch):
    if ch == "":
        return [ch]

    else:
        ensemble = []
        first_in = ch[0]
        for anagramme in sousEnsembles2(ch[1::]):
            ensemble += [anagramme, first_in + anagramme]

    return ensemble


def combinaisons2(ch, k):
    combs = [comb for comb in sousEnsembles2(ch) if len(comb) == k]
    return combs


def sousEnsembles1(ensemble):
    i, i_max = 0, 2 ** (len(ensemble)) - 1
    j, j_max = 0, len(ensemble) - 1
    sousensembles = []

    while i <= i_max:
        e = []
        while j <= j_max:
            if (i >> j) & 1 == 1:
                e.append(ensemble[j])
            j += 1
        sousensembles.append(e)
        j = 0
        i += 1
    return sousensembles


def combinaisons1(ensemble, k):
    i, i_max = 0, 2 ** (len(ensemble)) - 1
    j, j_max = 0, len(ensemble) - 1
    comb = []

    while i <= i_max:
        c = []
        if sum([int(i) for i in bin(i)[2::]]) == k:
            while j <= j_max:
                if (i >> j) & 1 == 1:
                    c.append(ensemble[j])
                j += 1
            comb.append(c)
            j = 0
        i += 1
    return comb


def sousEnsembles(L):
    if len(L) == 0:
        return [L]

    else:
        ensemble = []
        first_in = L[0]
        for anagramme in sousEnsembles(L[1::]):
            ensemble += [anagramme, [first_in] + anagramme]

    return ensemble


def combinaisons(L, k):
    combs = [comb for comb in sousEnsembles(L) if len(comb) == k]
    return combs


if __name__ == "__main__":
    # k = 3
    # chiffres = [i for i in range(20)]
    start = time()
    # combinaisons(chiffres, k)
    # print(combinaisons(chiffres, k))
    mid = time()
    # combinaisons1(chiffres, k)
    # print(combinaisons2(chiffres, k))
    print(combinaisons([0, 1, 2, 3], 2))
    end = time()
    print("dt = {} & dt1 = {}".format(mid - start, end - mid))
