#include "apremier.h"



bool isprime(int n)
{
    if (n < 2)
    {
        return false;
    }
    else if (n == 2 || n == 3)
    {
        return true;
    }
    else if (n % 2 == 0 || n % 3 == 0)
    {
        return false;
    }

    int k;
    for (k = 5; k * k <= n; k += 6)
    {
        if (n % k == 0 || n % (k + 2) == 0)
        {
            return false;
        }
    }

    return true;
}


/*
int main(){
    printf("test %d\n",isprime(25));  
    return 0;
}*/