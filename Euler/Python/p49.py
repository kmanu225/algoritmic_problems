from apremier import isprime


def candidates(m, n, p):
    # Check if m, n, and p are all distinct numbers
    if m == n or n == p or m == p:
        return False
    
    # Check if the differences between m and n and between n and p are equal
    if n - m == p - n:
        # Check if the digits in m, n, and p are the same (ignoring order)
        perm_m = set(str(m))
        perm_n = set(str(n))
        perm_p = set(str(p))
        if perm_m == perm_n == perm_p:
            return True

    return False


def solve():
    premiers = [p for p in range(1000, 10000) if isprime(p)]
    sol = []
    N = len(premiers)
    for m_i in range(N):
        m = premiers[m_i]
        for n_i in range(N):
            n = premiers[n_i]
            for p_i in range(N):
                p = premiers[p_i]

                if candidates(n, m, p):
                    sol.append([n, m, p])
    
    return sol


if __name__ == "__main__":
    solutions = solve()
    print(solutions)
