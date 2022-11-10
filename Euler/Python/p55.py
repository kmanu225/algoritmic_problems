from apalyndrome import isPal


def reverseAdd(nbr):
    return int(str(nbr)[::-1]) + nbr


count = 0
for nbr in range(1, 10001):
    for j in range(50):
        if isPal(reverseAdd(nbr)):
            count += 1
            break
        nbr = reverseAdd(nbr)


if __name__ == "__main__":
    # print(isPal(reverseAdd(201)))
    print(10000 - count)
