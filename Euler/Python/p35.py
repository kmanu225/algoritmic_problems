from apremier import isprime
from time import time

start = time()
lim = int(1e6)


def iscircular(n):
    if n in [2, 3, 5, 7]:
        return True

    if not isprime(n):
        return False

    for ch in "024568":
        if ch in str(n):
            return False

    nbreChiffres = len(str(n))
    nrot = 1
    while nrot <= nbreChiffres:
        if not isprime(int(str(n)[1::] + str(n)[0])):
            return False
        n = int(str(n)[1::] + str(n)[0])
        nrot += 1

    return True


if __name__ == "__main__":
    # print(iscircular(700001))
    sol = [i for i in range(2, lim + 1) if iscircular(i)]
    print("\nNombres premiers ciculaires en dessous de un million :\n", sol)
    print(
        "\nNombres de nombres premiers ciculaires en dessous de un million : {}\n".format(
            len(sol)
        )
    )
    end = time()
    print("temps d'exécution : {}\n".format(end - start))
