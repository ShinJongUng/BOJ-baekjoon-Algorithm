#include <stdio.h>
#define min(a,b)  (((a) < (b)) ? (a) : (b))

int main(void) { 
    long long a, b; 
    scanf("%lld %lld", &a, &b);
    if (a % 2 && b % 2) { 
        printf("%lld", min(a,b));
    } 
    else { 
        printf("0");
    } 
    return 0; 
}