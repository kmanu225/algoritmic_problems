
def pgcd(a, b):
    if a%b == 0:
        return b
    else :
        return pgcd(b, a%b)

def pgcdIt(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b


if __name__ == "__main__":
    print(pgcdIt(15, 21))
