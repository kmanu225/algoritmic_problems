import math


def SumDigFact(n):
    chiffres = str(n)
    som = 0

    for elt in chiffres:
        som += math.factorial(int(elt))

    return som


somme = 0
ensemble = {0, 1, 2}
limite = 1500000

for n in range(3, limite + 1):
    if SumDigFact(n) == n:
        ensemble.add(n)
        somme += n


if __name__ == "__main__":
    print(ensemble)
    print(somme)
    print(math.factorial(100))
