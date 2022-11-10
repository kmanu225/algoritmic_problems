""" Which starting number, under one million, produces the longest chain? """

from time import time


def collatz(n):
    if n % 2 == 1:
        return 3 * n + 1
    return n // 2


def len_collatz(n):
    length = 1
    while n != 1:
        n = collatz(n)
        length += 1

    return length


length = {1: 1, 2: 2, 4: 3}


def len_collatz_rec(n):
    if n in length.keys():
        return length[n]

    elif n % 2 == 0:
        length[n] = 1 + len_collatz_rec(n // 2)
    else:
        length[n] = 2 + len_collatz_rec((3 * n + 1) // 2)

    return length[n]


lim = 1000000
maxi = 0
winner = None
start = time()
for n in range(lim // 2, lim):
    if len_collatz_rec(n) > maxi:
        winner = n
        maxi = len_collatz_rec(n)
end = time()
print(winner, end - start)
