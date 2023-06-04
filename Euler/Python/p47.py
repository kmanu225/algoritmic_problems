from adivisors import divPremier

def solve():
    max_value = 1000000
    i = 30000
    n = 4
    while i < max_value:
        if all(len(divPremier(i + j)) == n for j in range(n)):
            return i
        i += 1
    return -1


if __name__ == "__main__":
    # print(solve())
    print(divPremier(134043), divPremier(134044),divPremier(134045))
