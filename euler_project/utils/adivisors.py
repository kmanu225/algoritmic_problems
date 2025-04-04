import math as m

from apremier import isprime


def nb_div(n):
    nb = 0
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0:
            nb += 2
    return nb


def div(n):
    divisors = {1}
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    divisors = list(divisors)
    divisors.sort()
    return divisors


def divStrict(n):
    diviseursStricts = div(n)
    diviseursStricts.remove(n)
    diviseursStricts.sort()

    return diviseursStricts


def sumDivStrict(n):
    return sum(divStrict(n))


def divPremier(n):
    divisors = []
    for i in range(1, int(m.sqrt(n)) + 1):
        if n % i == 0 and isprime(i):
            divisors.append(i)

    divisors.sort()
    return divisors


if __name__ == "__main__":
    n = 80
    print(divPremier(int("9" * n)))
