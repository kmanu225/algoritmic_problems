from time import time

start = time()
def digits(n):
    return [int(i) for i in list(str(n))]

def arePermutations(list1, list2):
    list1.sort(); list2.sort()

    return list1==list2


def permutedMultiples(n):
    nDigits = digits(n)
    Test = [digits(n*i) for i in range(2, 7)]
    #print(Test)
    for NDigits in Test:
        if not arePermutations(NDigits, nDigits):
            return False
    return True


def findSmallestSolution():
    n = 1
    while not permutedMultiples(n) :
        n+=1
    
    return n

if __name__== "__main__":
    print(findSmallestSolution())
    print("The program takes {}s".format(time()-start))
 