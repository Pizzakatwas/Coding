#include <stdio.h>
#include <string.h>

int main(){
    int array[]={9,5,4,3,13,20};
    int size = sizeof(array)/sizeof(array[0]);
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if (array[i]>array[j]){
                array[i]=array[i]+array[j];
                array[j]=array[i]-array[j];
                array[i]=array[i]-array[j];
            }
        }
    }
    for(int k=0;k<size;k++){
        printf("%d\n", array[k]);
    }
    return 0;
    }
