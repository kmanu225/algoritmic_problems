from apremier import isprime
from time import time

start = time()
lim = int(1e6)


def isTruncatable(n):
    if n in {2, 3, 5, 7}:
        return False

    nch1 = str(n)
    nch2 = str(n)
    while (len(nch1) != 0 and isprime(int(nch1))) and (
        len(nch2) != 0 and isprime(int(nch2))
    ):
        nch1 = nch1[1::]
        nch2 = nch2[: len(nch2) - 1]
        # print(nch1, nch2)
        if len(nch1) == 0 and len(nch2) == 0:
            return True

    return False


if __name__ == "__main__":
    sol = [i for i in range(lim) if isTruncatable(i)]
    print(
        "Les {} nombres premiers troncatables sont {}. Leur somme vaut {}.\n".format(
            len(sol), sol, sum(sol)
        )
    )
    print("Temps d'exécution : {}".format(time() - start))
