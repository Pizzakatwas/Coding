#include <stdio.h> // Hellow! Happy learning :
#include <math.h>
#include <ctype.h>

int main(){
    float temperature;
    float totemperature;
    char unit;
    char tounit;

    printf("Hello! This is a temp unit conversion program, what's the temperature?: ");
    scanf("%f", &temperature);
    printf("What's the unit of temperature?: ");
    scanf(" %c", &unit);
    printf("What do you want to convert it to?: ");
    scanf(" %c", &tounit);
    unit=tolower(unit);
    tounit=tolower(tounit);

    if(unit=='c'){
        if(tounit=='f'){
            totemperature=(temperature*9/5)+32;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else if(tounit=='k'){
            totemperature=temperature + 273.15;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else{
            printf("Please enter a valid unit!");
        }
    }
    else if(unit=='f'){
        if(tounit=='c'){
            totemperature=(temperature-32)*5/9;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else if(tounit=='k'){
            totemperature=(temperature-32)*5/9 + 273.15;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else{
            printf("Please enter a valid unit!");
        }
    }
    else if(unit=='k'){
        if(tounit=='f'){
            totemperature=(temperature-273.15)*9/5+32;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else if(tounit=='c'){
            totemperature=temperature -273.15;
            printf("Your conversion is:\n%.3f %c ==> %.3f %c", temperature, unit, totemperature,tounit);
        }
        else{
            printf("Please enter a valid unit!");
        }
    }

    return 0;
}