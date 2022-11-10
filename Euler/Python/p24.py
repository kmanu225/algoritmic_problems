from apermutation import *

chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
e = permutation(chiffres)
e = [colle(l) for l in e]


if __name__ == "__main__":
    print(e[1000000 - 1])
