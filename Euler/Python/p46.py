from apremier import isprime

def works(i, primes, squares_set):
    for j in primes:
        if (i - j) // 2 in squares_set:
            return True
    return False

def solve():
    max_value = 100000
    squares_set = set([n ** 2 for n in range(max_value)])
    primes = [n for n in range(max_value) if isprime(n)]

    odd_number = 3
    while works(odd_number, primes, squares_set):
        odd_number += 2

    print(odd_number)



    
if __name__ == '__main__':
    solve()