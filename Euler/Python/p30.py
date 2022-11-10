""" Find the sum of all the numbers that can be written as the sum of fifth powers of their digits. """


lim = 5
ensemble = []
for n in range(2, 5 * 9**5):
    l = list(str(n))
    l = [int(k) ** lim for k in l]
    if sum(l) == n:
        ensemble.append(n)

print(sum(ensemble), ensemble)
