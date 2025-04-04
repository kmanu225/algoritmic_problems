""" What is the value of the first triangle number to have over five hundred divisors?"""
from adivisors import nb_div

lim = 500
n = 1
while nb_div(n * (n + 1) // 2) < lim:
    n += 1

if __name__ == "__main__":
    print(n * (n + 1) // 2)
