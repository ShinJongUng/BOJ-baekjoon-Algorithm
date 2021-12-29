#include <stdio.h>

int main() {
    int n, cnt = 2;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        cnt += cnt - 1;
    }
    printf("%d\n", cnt*cnt);
    return 0;
}