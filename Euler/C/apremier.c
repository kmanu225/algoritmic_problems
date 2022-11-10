#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include "apremier.h"


bool isprime(long n){
    if(n<2){
        return 0;
    }

    else if((n==2) || (n == 3)){
        return 1;
    }

    else if ((n%2==0) || (n%3==0)) {
        return 0;
    }

    else {
        
        for (int i = 5; i<sqrt(n)+1; i++){
            if (n%i == 0) {
                return 0;
            }
        }

        return 1;

    }
    
}


/*
int main(){
    printf("test %d\n",isprime(25));  
    return 0;
}*/