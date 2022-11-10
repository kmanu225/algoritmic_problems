from typing import List


def sur_les_ondes(n: int, freqs: List[int]) -> None:
    """
    :param n: nombre de fréquences données
    :param freqs: la liste des fréquences à vérifier
    """
    # TODO Afficher la fréquence optimale.
    if n == len(freqs) :
        print(min([nb for nb in freqs if nb % 3 == 0]))

    else:
        print(f"You have do enter {n} number in the terminal with a single spacing between them.")


if __name__ == "__main__":
    n = int(input())
    freqs = list(map(int, input().split()))
    sur_les_ondes(n, freqs)
