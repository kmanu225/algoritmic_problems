""" What is the index of the first term in the Fibonacci sequence to contain 1000 digits? """

fibbo_cache = {1: 1, 2: 1}


def fibbo(n):
    if n in fibbo_cache:
        return fibbo_cache[n]

    fibbo_cache[n] = fibbo(n - 1) + fibbo(n - 2)
    return fibbo_cache[n]


n = 1
while len(list(str(fibbo(n)))) != 1000:
    n += 1
print("n = {}\nF(n) = {}".format(n, fibbo(n)))
