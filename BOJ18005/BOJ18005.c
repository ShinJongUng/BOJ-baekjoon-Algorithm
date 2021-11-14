#include <stdio.h>
int main(void) { 
    int n; 
    scanf("%d", &n);
    int result;
    if (n % 2) { 
        result = 0; 
    } 
    else 
    { 
        if ((n / 2) % 2) { 
            result = 1; 
        } 
        else 
        { 
            result = 2; 
        } 
    }
    printf("%d", result);
}

