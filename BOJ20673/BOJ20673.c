#include <stdio.h>
 
int main(void) { 
    int p, q; 
    scanf("%d %d", &p, &q);
    if (50 >= p && 10 >= q) { 
         printf("White");
    } 
    else if (30 <= q) {
        printf("Red");
    } 
    else { 
        printf("Yellow");
    } 
    return 0;
}
