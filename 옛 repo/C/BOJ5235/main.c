#include <stdio.h>
int main(void) { 
    int T; 
    scanf("%d", &T);
    for (int t = 0; t < T; t++) { 
        int k; 
        scanf("%d", &k);
        int evenSum = 0, oddSum = 0; 
        for (int i = 0; i < k; i++) { 
            int num; 
            scanf("%d", &num);
            if (num % 2) { 
                oddSum += num; 
                continue; 
            } evenSum += num; 
        } 
        if (evenSum > oddSum) { 
            printf("EVEN\n");
        } 
        else if (evenSum == oddSum) { 
            printf("TIE\n");
        } 
        else { 
            printf("ODD\n");
        } 
    } 
    return 0; 
}
