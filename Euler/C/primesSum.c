#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "apremier.h"
long find(long pMax, long longMax);
long find(long pMax, long longMax){
    
    long lim = 1000000;
    int sup = 13;

    //On défini les nombres premiers inférieur à sup=10 dans le tableau premiers.
    long premiers[sup];
    long p=2;
    int len = 0;
    for(p=2; p<=sup; p++){
        if(isprime(p) == 1){
            premiers[len] = p;
            //printf("%ld\n", p);
            len++;
        }
    }
    
    int n = 0;
    int i = 0;
    //printf("%ld %ld\n",premiers[2],premiers[3]);

    //Recherche de la somme maximale et de la longueur maximale de la suite
    while(n<len){

        //Recherche de la somme maximale et de la longueur maximale de la suite en commençant la suite à premiers[n]
        long pmax = 0;
        long som = 0;
        i=premiers[n];
        int length = 0;
        int lmax = 0;
        while(som<=lim) {
            if (isprime(i) == 1) {
                som += i;
                length++;
                printf("%d\n", i);
            }

            //Mise à jour du maximum local
            if (isprime(som) == 1) {
                pmax = som;
                lmax = length;
                
                
            }
            i++;
        }

        
        //Mise à jour du maximum global
        if ((lim>=pmax) && (pmax>pMax) && (lmax>longMax)) {
            pMax = pmax;
            longMax = lmax;
        }
        
        n++;// On passe à une nouvelle initialisation pour la suite.
    }
    return pMax;
    
}
    
    


int main(){
    // long pMax=0;
    // long longMax=0;
    // pMax = find(pMax, longMax);
    // printf("je suis %ld\n", pMax);
    printf("%d", isprime(929393));
    return 0;
    
}