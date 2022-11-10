""" 
Find the difference between the sum of the squares of the first lim natural numbers and the square of the sum 
"""
lim = 100
print(sum([i for i in range(lim + 1)]) ** 2 - sum([i**2 for i in range(lim + 1)]))
