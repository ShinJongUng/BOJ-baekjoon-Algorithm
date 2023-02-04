#include <stdio.h>

int main(void) {
    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);

    int max = 0;
    while (N >= 2 && M >= 1) {
        N -= 2;
        M--;
        max++;
    }
    while (N + M < K) {
        N += 2;
        M++;
        max--;
    }

    printf("%d", max);
}