def t(n):
    return n * (n + 1) // 2


def p(n):
    return n * (3 * n - 1) // 2


def h(n):
    return n * (2 * n - 1)


def solve():
    i_t = 286
    i_p = 166
    i_h = 144
    max = 1000000000
    while i_t < max:
        while p(i_p) <= t(i_t):
            while h(i_h) <= p(i_p):
                if t(i_t) == p(i_p) and t(i_t) == h(i_h):
                    return [t(i_t), p(i_p), h(i_h)]
                i_h += 1
            i_p += 1
        i_t += 1

    print("didn't find the solution under", [i_t, i_p, i_h])
    return "try again"


if __name__ == "__main__":
    sol = solve()
    print(sol)
