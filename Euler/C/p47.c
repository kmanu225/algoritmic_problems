#include "apremier.h"

int *divPremier(int n, int *length)
{
    if (isprime(n))
    {
        int *divisors = malloc(sizeof(int));
        divisors[0] = n;
        *length = 1;
        return divisors;
    }

    int *divisors = malloc(n * sizeof(int));
    int count = 0;
    for (int i = 1; i < n; i++)
    {
        if (isprime(i) && n % i == 0)
        {
            divisors[count] = i;
            count++;
        }
    }

    int *result = realloc(divisors, count * sizeof(int));
    *length = count;
    return result;
}

int solve()
{
    int max_value = 1000000;
    int i = 1;
    int n = 4;
    while (i < max_value)
    {
        bool allDivisorsN = true;
        for (int j = 0; j < n; j++)
        {
            int length;
            int *divisors = divPremier(i + j, &length);
            if (length != n)
            {
                allDivisorsN = false;
                break;
            }
            free(divisors);
        }

        if (allDivisorsN)
        {
            return i;
        }
        i++;
    }

    return -1;
}

int main()
{
    printf("%d\n", solve());
    return 0;
}
