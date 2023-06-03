import numpy as np

n = 5


def spmat(n):
    m = np.eye(n, n)
    i1, j1 = 0, 0
    for cycle in range((n + 1) // 2):

        val1 = n * (n - 1) + 1

        while i1 < n:
            m[i1][j1] = val1
            val1 -= 1
            i1 += 1
        i1 = 1
        j1 = i1
        n -= 1

    return m


print(spmat(5))


# val1 = n*(n-1)
# val2 = n*(n-2)
# val3 = n*(n-3)
# val4 = n*(n-4)


print(len(np.eye(101, 101)))
