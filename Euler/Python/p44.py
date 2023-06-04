# Pentagon Numbers
max = 20000
valides = set()


def p(n):
    return int(n * (3 * n - 1) / 2)


def solve():
    minD = float("inf")
    for i in range(1, max + 1):
        pi = p(i)
        for j in range(i + 1, max + 1):
            pj = p(j)

            if pj + pi in suite and pj - pi in suite:
                valides.add((i, j))
                diff = pj - pi
                if diff < minD:
                    minD = diff

    print(valides)
    print(minD)


if __name__ == "__main__":
    suite = set([p(n) for n in range(1, 4 * max + 1)])
    # print(suite)
    solve()
    # print(p(2167)-p(1020), p(2167)+p(1020))
    # i = 0
    # while p(i)!=5482660 :
    #     i+=1
    # print(i)
    # while p(i)!=8602840 :
    #     i+=1
    # print(i)
