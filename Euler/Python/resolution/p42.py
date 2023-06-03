from time import time

start = time()
fichier = open("p42_words.txt", "r")
words = []

for line in fichier.readlines():
    words += line.split(",")

fichier.close()
words = [name[1:-1] for name in words]


def wordValue(word):
    score = 0
    for letter in word:
        score += ord(letter) - 64
    return score


def isTriangle(word):
    score = wordValue(word)
    n = 1
    while n * (n + 1) // 2 < score:
        n += 1
        if n * (n + 1) // 2 > score:
            return False

    return True


if __name__ == "__main__":
    nbre = 0
    for word in words:
        if isTriangle(word):
            nbre += 1
            # print(word, wordValue(word))
    print("Nomnre de mots triangles : {}\n".format(nbre))
    print("temps d'exécution : {}".format(time() - start))
