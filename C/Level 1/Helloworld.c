#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int fact(int x){
    if(x=0){
        return 1;
    } 
    else if(x>0){
        return x*fact(x-1);
    }
}

int main(){
    float x;
    float sum;
    int n;

    printf("%d", fact(4));


    return 0;
}