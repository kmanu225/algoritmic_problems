
from typing import List




def mise_en_boite(n: int, restes: List[int], boites: List[int]) -> None:
    """
    :param n: Le nombre de boîtes et de restes
    :param restes: Liste des volumes des restes
    :param boites: Liste des volumes des boîtes
    """
    # TODO Afficher sur une ligne le nombre maximum de restes que l'on peut
    # mettre en boîte.
    #print(restes, boites)

    restes.sort(); boites.sort()
    i = 0
    for reste in restes[::-1]:
        if reste<= max(boites):
            boites.pop()
            i+=1
    print(i)



if __name__ == "__main__":
    n = int(input())
    restes = list(map(int, input().split()))
    boites = list(map(int, input().split()))
    mise_en_boite(n, restes, boites)
