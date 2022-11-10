""" 
Find the sum of all the multiples of d1 and d2 below lim
"""


def som_multiple(d1, d2, lim):
    som = 0
    for nombre in range(min([d1, d2]), lim):
        if nombre % d1 == 0 or nombre % d2 == 0:
            som += nombre
    return som


if __name__ == "__main__":
    print(som_multiple(3, 5, 1000))
