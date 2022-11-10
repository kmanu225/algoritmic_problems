import math as m

size = 9
s = [0] * size

# validation des propriétés de l'enoncé
def check(L):
    Pl = []
    Pc = []
    diagonal1 = []
    diagonal2 = []
    columns = []
    lignes = []
    m = 0
    for diag in range(len(L)):
        diagonal1.append(L[diag][diag])
    for andiag in range(len(L) - 1, -1, -1):
        diagonal2.append(L[m][andiag])
        m += 1
    for lig in range(len(L)):
        for col in range(len(L)):
            lignes.append(L[lig][col])
        Pl.append(lignes)
        lignes = []
    for coln in range(len(L)):
        for lign in range(len(L)):
            columns.append(L[lign][coln])
        Pc.append(columns)
        columns = []

    # print(diagonal2)
    for i in range(len(L)):
        if (
            sum(Pc[i]) == sum(Pl[i])
            and sum(Pc[i]) == sum(diagonal1)
            and sum(diagonal1) == sum(diagonal2)
        ):
            continue
        else:
            return False

    return True


# transformation d'une liste en une liste de 3 listes
def transf(L):
    k = list(L)
    M = []
    n = int(m.sqrt(len(L)))
    for i in range(n):
        M.append(k[:n])
        k = k[n:]
    return M


# ajout des solutions qui marchent dans la liste L
L = []


def solution(pos):
    if pos >= size:
        # print(L)
        if check(transf(s)) == True:
            L.append(s.copy())

    else:
        for value in range(1, size + 1):
            if value not in s:
                s[pos] = value
                solution(pos + 1)
                s[pos] = 0

    return L


if __name__ == "__main__":
    # print(check(transf([8, 6, 1, 4, 2, 9, 3, 7, 5])))
    # print(len([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print(solution(0), len(L))
