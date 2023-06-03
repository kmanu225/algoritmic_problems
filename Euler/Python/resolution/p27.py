from apremier import isprime
import numpy

alim = 999
blim = 1000

bValues = [b for b in range(blim + 1) if isprime(b)]
aValues = list({a for a in range(-alim, alim + 1)}.difference(set(bValues)))


def quadratic(a, b, n):
    return n**2 + a * n + b


def find(A=aValues, B=bValues):
    a, b = None, None
    n_max = 0

    for bi in bValues:
        for ai in aValues:

            if ai**2 - 4 * bi > 0:
                pass

            nlim = numpy.inf
            if bi - ai >= 0:
                # print(ai, bi)
                nlim = bi - ai

            n = 0
            while isprime(quadratic(ai, bi, n)) and nlim > n:
                n += 1
                if n >= n_max:
                    n_max = n
                    a, b = ai, bi

    return a, b, a * b, n_max


if __name__ == "__main__":
    # print(aValues)
    print(find())
