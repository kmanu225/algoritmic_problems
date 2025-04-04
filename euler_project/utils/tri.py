def qsort(L):
    if L == []: 
        return []
    return qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])





def fusion(liste_1: list, liste_2: list)->list:
    merged = []
    lgth_1 = len(liste_1)

    for i in range(lgth_1):
        val_1 = liste_1[i]
        while liste_2!=[] and val_1 > liste_2[0]:
            merged.append(liste_2.pop(0))
        merged.append(val_1)

    merged+=liste_2
    return merged

def fusion_ite(liste_1: list, liste_2: list) -> list:
    merged = []
    lgth_1 = len(liste_1)
    lgth_2 = len(liste_2)
    i = j = 0
    while i < lgth_1 and j < lgth_2:
        if liste_1[i] < liste_2[j]:
            merged.append(liste_1[i])
            i += 1
        else:
            merged.append(liste_2[j])
            j += 1
    merged += liste_1[i:]
    merged += liste_2[j:]
    return merged

def fusion_rec(liste_1: list, liste_2: list)->list:
    if len(liste_1) == 0:
        return liste_2
    elif len(liste_2) == 0:
        return liste_1
    
    else: 
        if liste_1[0]>liste_2[0]:
            return [liste_2[0]]+fusion_rec(liste_1, liste_2[1::])
        else:
            return [liste_1[0]]+fusion_rec(liste_1[1::], liste_2)

def tri_fusion(liste: list)->list:
    n = len(liste)
    if n<=1:
        return liste
    else:
        return fusion(tri_fusion(liste[:n//2]), tri_fusion(liste[n//2:]))
