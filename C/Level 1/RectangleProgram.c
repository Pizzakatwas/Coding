#include <stdio.h>

int main(){
    int x;
    int y;
    char character;

    printf("Hey! This is a program that prints out rectangles of cool characters, what's your character?: ");
    scanf("%c", &character);
    printf("How many lines?: ");
    scanf("%d", &x);
    printf("How many columns?: ");
    scanf("%d", &y);

    for(int i=1;i<=x;i++){
        for(int j=1;j<=y;j++){
            printf("%c", character);
        }
        printf("\n");
    }


    return 0;
}
