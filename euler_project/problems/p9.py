""" There exists exactly one Pythagorean triplet for which a + b + c = lim. Find the product abc. """
import math as m


def pyth_triplet(lim):
    for a in range(1, m.ceil(lim / 3)):
        for c in range(m.ceil(lim / 3), lim):
            if a**2 + (lim - a - c) ** 2 == c**2:
                return {"a": a, "b": lim - a - c, "c": c}


print(pyth_triplet(1000))
print(425 * 200 * 375)
