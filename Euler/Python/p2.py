""" 
By considering the terms in the Fibonacci sequence whose values do not exceed lim, find the sum of the even-valued terms. 
"""
lim = 4e6
f1 = 1
f2 = 2
som = 2
while f1 + f2 < lim:
    if (f1 + f2) % 2 == 0:
        som += f1 + f2
    f1, f2 = f2, f1 + f2

if __name__ == "__main__":
    print(som)
