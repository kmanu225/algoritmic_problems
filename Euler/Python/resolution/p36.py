""" Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2. """


lim = int(1e6)


def pal10_2(nbr):
    return (
        list(str(nbr)) == list(str(nbr))[::-1]
        and bin(nbr)[2::] == bin(nbr)[len(bin(nbr)) : 1 : -1]
    )


def find():
    pald = []
    som = 0
    for nb in range(lim):
        if pal10_2(nb):
            pald.append(nb)
            som += nb
    return pald, som


print(find())
print(pal10_2(585585585))
