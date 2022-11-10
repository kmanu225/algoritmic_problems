# Ensemble des permutations d'une liste notée L


def transform(l):
    nbr = ""
    for n in l:
        nbr += n
    return int(nbr)


def permutation(L):
    if len(L) <= 1:
        return [L]

    else:

        ensemble = []
        l = list(L)

        for i in range(len(L)):
            first_in = l.pop(i)

            for anagramme in permutation(l):
                if anagramme not in ensemble:
                    ensemble.append(anagramme)
                if [first_in] + anagramme not in ensemble:
                    ensemble.append([first_in] + anagramme)

            l = list(L)

        return ensemble


ensemble = permutation(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

for i in range(len(ensemble)):
    ensemble[i] = transform(ensemble[i])

# print(permutation(['1','2','4','3']))
ensemble.sort()
print(ensemble, len(ensemble))
