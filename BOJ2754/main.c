#include <stdio.h>

int main() {
    char n1, n2;
    double score = 0;
    scanf("%c%c", &n1,&n2);
    if(n1 == 'A')
        score = 4;
    if(n1 == 'B')
        score = 3;
    if(n1 == 'C')
        score = 2;
    if(n1 == 'D')
        score = 1;
    if(n1 == 'F')
        score = 0;
    if(n2 == '+')
        score += 0.3;
    else if(n2 == '-')
        score -= 0.3;
    
    printf("%.1lf", score);
}
