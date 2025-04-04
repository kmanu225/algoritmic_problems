""" What is the largest prime factor of the number lim ? """
import math as m
from apremier import isprime

lim = 600851475143


primes = [i for i in range(20000 + 1) if isprime(i)]
maxi_div = None
for p in primes:
    if lim % p == 0:
        maxi_div = p

# coup de bole
print(maxi_div)

print(m.sqrt(lim))
