from time import time


def colle(
    l,
):  # assemble les nombres d'une liste pour former un nombre : ["1", "2", "3"] --> 123
    nbr = ""
    for n in l:
        nbr += n
    return nbr  # int(nbr)


def permutation(L):
    if len(L) <= 1:
        return [L]

    else:
        ensemble = []
        l = list(L)
        for i in range(len(L)):
            first_in = l.pop(i)
            for anagramme in permutation(l):
                ensemble.append([first_in] + anagramme)
            l = list(L)
    return ensemble


def permutation1(ch):
    if len(ch) <= 1:
        return [ch]
    else:

        ensemble = []
        l = ch
        for i in range(len(ch)):
            first_in = l[i]
            l = l[:i] + l[i + 1 :]
            for anagramme in permutation1(l):
                ensemble.append(first_in + anagramme)
            l = ch
    return ensemble


L = []
size = 3
elt = [-1] * size


def permutation2(pos):
    if pos >= size:
        L.append(colle(elt.copy()))

    else:
        for value in range(size):
            if str(value) not in elt:
                elt[pos] = str(value)
                permutation2(pos + 1)
                elt[pos] = "-1"
    return L


L = []
size = 3
elt = [0] * size


def permutation3(pos):
    if pos >= size:
        L.append(elt.copy())

    else:
        for value in range(1, size + 1):
            if str(value) not in elt:
                elt[pos] = str(value)
                permutation3(pos + 1)
                elt[pos] = "0"
    return L


# if __name__ == "__main__" :
# start = time()
# L = [i for i in range(10)]
# permutation(L)
# mid = time()
# permutation2(0)
# end = time()
# print("dt1 = {} & dt2 = {}".format(mid-start, end-mid))
# print(permutation1("123"))
# l = "123456789"
# i=3
# first_in = l[i]
# l = l[:i]+l[i+1:]
# print(l)
