import decimal
from apgcd import pgcd


#The serie we define converge toward sqrt(2)
def sqrt2(n):
    sqrt = 1
    for i in range(n):
        sqrt = 1+1/(1+sqrt)

    return sqrt


def extractDenNum(fract):
    decimal_object = decimal.Decimal(fract)
    return decimal_object.as_integer_ratio()



if __name__ == "__main__":
    print(extractDenNum(sqrt2(8)))
    print(pgcd(6369061237727393,4503599627370496))
    
