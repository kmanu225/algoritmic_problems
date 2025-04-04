from apremier import isprime
from time import time

start = time()

premiers = [p for p in range(1000, 10000) if isprime(p)]
premiersStr = []
for p in premiers:
    l = list(str(p))
    l.sort()
    premiersStr.append("".join(l))


dico = {p: [] for p in premiers}
candidate = []
n = len(premiers)
for i in range(n):
    if i >= len(premiers):
        break


if __name__ == "__main__":
    # print(candidate)
    print(premiers)
    print(premiersStr)
    print(dico)
