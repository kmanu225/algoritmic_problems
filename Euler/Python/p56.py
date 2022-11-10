"""Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum"""

lim = 100
som_max = 0


def somme_nb(nb):
    l = list(str(nb))
    l = [int(ch) for ch in l]
    return sum(l)


for a in range(1, 101):
    for b in range(1, 101):
        if somme_nb(a**b) > som_max:
            x = a
            y = b
            som_max = somme_nb(a**b)

print(som_max, "a=", x, "b=", y, 99**95)
