from apermutation import permutation, colle, permutation1
from time import time

start = time()
# V0
premiers = [2, 3, 5, 7, 11, 13, 17]
chiffres = "0123456789"


def elegible(pan):
    part = [int(pan[i : i + 3]) for i in range(1, 8)]
    for i in range(7):
        if part[i] % premiers[i] != 0:
            return False
    return True


selected = [int(pan) for pan in permutation1(chiffres) if elegible(pan)]


# V1
# n =3
# chiffres = [str(i) for i in range(n)]
# premiers = [2, 3, 5, 7, 11, 13, 17]
# pandigitals = [pan for pan in permutation(chiffres)]
# print(pandigitals)

# def find(pandig = pandigitals) :
#     selected = []
#     for pan in pandig :
#         if elegible(pan) :
#             selected.append(int(pan))

#     print("Les pandigitals qui respectent la propriété sont : {}, leur somme vaut {}.".format(selected, sum(selected)))
#     return selected, sum(selected)


# V2
# L = []
# size = 10
# elt = [-1]*size
# def find(pos=0):
#     if pos >= size and elegible(colle(elt.copy())):
#         L.append(int(colle(elt.copy())))

#     else:
#         for value in range(size):
#             if str(value) not in elt:
#                 elt[pos] = str(value)
#                 find(pos+1)
#                 elt[pos] = '-1'
#     return L

if __name__ == "__main__":
    # find() #V1
    # selected = find() #V2
    print(
        "Les pandigitals qui respectent la propriété sont : {}, leur somme vaut {}.".format(
            selected, sum(selected)
        )
    )
    end = time()
    print("temps d'exécution : {} secondes".format(round(end - start, 2)))
