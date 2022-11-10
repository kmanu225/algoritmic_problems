chiffres = [i for i in range(1, 10)]
triplet = []


# Construction de nos triplets
while len(triplet) <= 120 and len(chiffres) >= 3:
    chiffres1 = chiffres
    chiffres2 = chiffres
    chiffres3 = chiffres
    for i1 in chiffres1:
        for i2 in chiffres2:
            for i3 in chiffres3:
                if i1 != i2 and i1 != i3 and i2 != i3:
                    if {i1, i2, i3} not in triplet:
                        triplet.append({i1, i2, i3})
    chiffres = chiffres[1::]


triplet2 = [list(t) for t in triplet]
for l in triplet2:
    l.sort()

# Calcul des sommes de chaque triplet
som = [[l, sum(l)] for l in triplet2]
som2 = [l[1] for l in som]

# Recherche des triplets qui donnent la même somme
# dico : key=somme, value=[[triplet de mm somme], nombre de triplets de la même somme]
dico = {}

for i in range(24):
    for j in range(len(som2)):
        if som2[j] == i and (som2[j] not in dico.keys()):
            dico[i] = [[j], 1]
        elif som2[j] == i and (som2[j] in dico.keys()):
            dico[i][0].append(j)
            dico[i][1] += 1

print(dico)


# On prend dans dico les listes où on a 8 triplets de même valeurs.
p1 = [17, 20, 22, 33, 37, 40, 51, 54]  # somme = 14
p2 = [21, 23, 38, 41, 43, 52, 55, 64]  # somme = 15
p3 = [24, 25, 42, 44, 53, 56, 58, 65]  # somme = 16


# Vérification des possibilités


def verf(p):
    dico_v = {k: 0 for k in range(1, 10)}
    for i in range(8):
        for k in dico_v.keys():
            if k in triplet2[p[i]]:
                dico_v[k] += 1
    i += 1
    return dico_v


# Le pivot doit apparaître 4 fois(seule la solution 2 marche, 5 est le pivot)
verf(p1)
verf(p2)
verf(p3)

# Solution
verf(p2)

for i in p2:
    print(triplet[i])

# On construit le tableau avec les deux affichages précédents
