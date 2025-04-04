from time import time
from adivisors import sumDivStrict

start = time()
lim = 28123
abundants = []
for n in range(12, lim + 1):
    if sumDivStrict(n) > n:
        abundants.append(n)

somAbundants = {24}
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= lim:
            somAbundants.add(abundants[i] + abundants[j])

somNotSomAbundants = lim * (lim + 1) // 2 - sum(somAbundants)


if __name__ == "__main__":

    print(somNotSomAbundants)
    print(time() - start)
