#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

void player(char x, char y[]){
    int lock4 = 1;
    int choice;  
    do {
        printf("\nSelect a spot: \n");
        scanf("%d", &choice);
        if(choice<10 && choice>0){
            break;
        }
    } while(true);
    while( y[choice-1]=='X' || y[choice-1]=='O' ){
        printf("That spot is already taken!\nSelect a spot: ");
        scanf("%d", &choice);
    }
    y[choice-1] = x;
    lock4 = 1;
    

}

void computerc(char x, char y[]){
    int random = rand()%9;
    while( y[random]=='X' || y[random]=='O' ){
        random = rand()%9;
    }
    y[random] = x;
}

int check(char game[]){
    for(int i=0;i<3;i++){
        if((game[i*3]==game[i*3+1] && game[i*3+1]==game[i*3+2]) || (game[i]==game[i+3] && game[i+3]==game[i+6]) || (game[0]==game[4] && game[4]==game[8]) || (game[6]==game[4] && game[4]==game[2])){
            return 1;
        }
    }
    return 0;
}

void refresh(char game[]){
    printf("\n\n%c | %c | %c\n", game[0], game[1],game[2]);
    printf("---------\n");
    printf("%c | %c | %c\n", game[3], game[4],game[5]);
    printf("---------\n");
    printf("%c | %c | %c\n\n", game[6], game[7],game[8]);

}

int main(){
    int counter=0;
    char character;
    char computer;
    char start;
    int lock1 = 1;
    int lock2 = 1;
    int lock3 = 1;
    char game[] = {'1','2','3','4','5','6','7','8','9'};
    bool running = true;
    bool again = true;
    char againc;
    srand(time(0));

    printf("Welcome to Rabii's TTT\n");


    while(lock1 == 1){

        printf("\nPlease choose your character (X/O): ");
        scanf(" %c", &character);
        character = toupper(character);

        if(character!='X' && character!='O'){
            printf("Not a valid character!");
            continue;
        }
        lock1 = 0;
    }
    while(lock2 == 1){

        printf("\nDo you want to start first? (Y/N): ");
        scanf(" %c", &start);
        start = tolower(start);

        if(start!='y' && start!='n'){
            printf("Not a valid answer!");
            continue;
        }
        lock2 = 0;
    }

    printf("Let the game (making) begin!");

    if(character=='X'){
        computer='O';
    } else{
        computer='X';
    }

    while(again){
        lock3 = 1;
        char game[] = {'1','2','3','4','5','6','7','8','9'};
        refresh(game);
        while(running){

            if(start == 'y'){
                player(character, game);
                counter++;
                if(check(game)){
                    refresh(game);
                    printf("The game has ended!\n");
                    printf("The winner is the player!");
                    running = false;
                    break;
                }
                if(counter==9){
                    printf("There are no spots left! The game has ended!\nIt's a draw!\n");
                    running = false;
                    break;
                }
                computerc(computer, game);
                counter++;
                if(check(game)){
                    refresh(game);
                    printf("The game has ended!\n");
                    printf("The winner is the computer!");
                    running = false;
                    break;
                }
                refresh(game);
            }
            else{
                computerc(computer, game);
                refresh(game);
                counter++;
                if(check(game)){
                    refresh(game);
                    printf("The game has ended!\n");
                    printf("The winner is the computer!");
                    running = false;
                    break;
                }
                if(counter==9){
                    printf("There are no spots left! The game has ended!\nIt's a draw!\n");
                    running = false;
                    break;
                }
                player(character, game);
                counter++;
                if(check(game)){
                    refresh(game);
                    printf("The game has ended!\n");
                    printf("The winner is the player!");
                    running = false;
                    break;
                }
                refresh(game);
            }
        }


        
    while(lock3 == 1){
        counter = 0;
        printf("\nDo you want to try again? (Y/N): ");
        scanf(" %c", &againc);
        again=tolower(againc);

        if(againc != 'y' && againc != 'n'){
            printf("\nPlease choose a valid answer!");
            continue;
        }

        if(againc=='y'){
            printf("Which character?: ");
            scanf(" %c", &start);
            start=tolower(start);
            running = true;
            again = true;
        } else {
            again = false;
        }

        lock3 = 0;
    }
        
    }
    
    printf("Thanks for playing :)!, and thanks me for making the game :D");

    return 0;
}

// 2 hours lol