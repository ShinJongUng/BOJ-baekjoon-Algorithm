#include <stdio.h>


double GALLON2LITER = 3.785411784;
double MILE2KM = 1.609344;
double HUNDRED_KM = 100.00;

int main() { 
    double milesPerGallon; 
    scanf("%lf", &milesPerGallon); 
    double result = HUNDRED_KM / ((MILE2KM / GALLON2LITER) * milesPerGallon); 
    printf("%.6lf\n", result); 
    return 0; 
}

