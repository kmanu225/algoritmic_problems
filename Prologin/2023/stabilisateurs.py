from typing import List


def stabilite_maximale(n: int, k: int, p: int, accroches: List[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
  
    accroches.sort()


    stabiliteOptimale = 0
    groupOptimal = []

    for i in range(0, 4*n//4-3):
        cp = list(accroches)[i::]
        group = []
        stabilite = 0
        while len(cp) >= 4:

            part = cp[0:4]
            if p - (part[-1]-part[0])**2 >= 0 :
                stabilite += p - (part[-1]-part[0])**2
                group.append(part)

            cp = cp[4::]

        if stabiliteOptimale < stabilite and len(group)<=k:
            stabiliteOptimale = stabilite
            groupOptimal = group
    
    print(len(groupOptimal))



if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
