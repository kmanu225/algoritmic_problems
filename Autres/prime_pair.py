import math as m
import time


def is_prime(n):
    if n == 1:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False

    else:
        i = 5
        while i <= m.ceil(m.sqrt(int(ch))):
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
            i += 6
        return True


def is_prime1(ch):
    if int(ch) == 1:
        return False
    elif int(ch) == 2:
        return True
    else:
        for i in range(2, m.ceil(m.sqrt(int(ch))) + 1):
            if int(ch) % i == 0:
                return False
        return True


def is_comb_prime(L):

    for i in L:
        P = []
        for k in L:
            if k != i:
                P.append(k)
        if is_comb_prime_num(i, P) == False:
            return False

    return True


def is_comb_prime_num(ch, L):
    if L == []:
        return True
    else:
        for p in L:
            a = ch + p
            b = p + ch
            if is_prime(a) == True and is_prime(b) == True:
                continue
            else:
                return False

        return True


def is_comb_prime_num1(ch, L):
    if L == []:
        return True
    else:
        for p in L:
            a = ch + p
            b = p + ch
            if is_prime1(a) == True and is_prime1(b) == True:
                continue
            else:
                return False

        return True


"""
def transf1(ch):
    L = []
    for p in ch:
        L.append(p)
    return L

def transf2(L):
    ch = ""
    for k in L:
        ch += k
    return ch 

def gen(ch,size,L):
    if len(ch) >= size:
        if is_prime(ch) == True and ch[0] != "0":
            L.append(ch)
        return
    else:
        for i in range(10):
            ch += str(i)
            gen(ch,size,L)
            p = transf1(ch)
            p.pop()
            ch = transf2(p)
        
        return

    
def prime_set(size):
    L = []
    K = []
    for i in range(1,size+1):
        gen("",i,L)
        
    K.extend(L)
        
    return K
"""


def gen_prime(n):
    L = [str(i) for i in range(2, n + 1) if is_prime(i)]
    return L


def gen_prime1(n):
    L = [str(i) for i in range(2, n + 1) if is_prime1(i)]
    return L


def min_prime(Lprimes, limit, H, P):
    if len(H) >= limit:
        # print(H)
        P.append(H.copy())
        return True
    else:
        for i in range(len(Lprimes)):
            if Lprimes[i] not in H and is_comb_prime_num(Lprimes[i], H):
                H.append(Lprimes[i])
                if min_prime(Lprimes, limit, H, P) == True:
                    return True
                H.pop()

        return False


def min_prime1(Lprimes, limit, H, P):
    if len(H) >= limit:
        # print(H)
        P.append(H.copy())
        return True
    else:
        for i in range(len(Lprimes)):
            if Lprimes[i] not in H and is_comb_prime_num1(Lprimes[i], H):
                H.append(Lprimes[i])
                if min_prime(Lprimes, limit, H, P) == True:
                    return True
                H.pop()

        return False


if __name__ == "__main__":
    # print(is_prime("67217"))
    start = time.time()
    P = []

    L = gen_prime(10000)

    L.remove("5")
    min_prime(L, 5, [], P)
    diff1 = time.time() - start

    # start1 = time.time()

    # P = []

    # L = gen_prime1(10000)

    # L.remove("5")
    # min_prime1(L,5,[],P)
    # diff2 = time.time() - start1
    print(f"{diff1} secondes:version ameliorée")

    """
    start = time.time()
    gen_prime(1000)
    diff1 = time.time() - start
    start1 = time.time()
    gen_prime1(1000)
    diff2 = time.time() - start1
    print(f"{diff1} secondes:version ameliorée / {diff2} secondes: version ancienne")
    """

    # print(is_comb_prime(["3","7","11","17","19"]))
