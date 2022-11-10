from typing import List

def distance(redirection, depart):
    d = 0
    visite = [depart]
    while redirection[visite[-1]-1] not in visite :
        visite.append(redirection[visite[-1]-1])
        d+=1
    return d+1

def trajets_retour(n: int, redirection: List[int]) -> None:
    """
    :param n: le nombre de cinémas
    :param redirection: le lieu de redirection de chaque cinéma
    """
    for depart in range(n):
       print(distance(redirection, depart+1), end=" ")



if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    trajets_retour(n, redirection)