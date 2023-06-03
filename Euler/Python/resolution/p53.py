import math as m

lim = int(1e6)
i = 0


n_max = 100
for n in range(n_max + 1):
    for r in range(n):
        if m.comb(n, r) > lim:
            i += 1

print(i)
