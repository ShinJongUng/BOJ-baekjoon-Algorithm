#include <stdio.h>
int arr[100001] = { 0, };
int main() {
    int n, temp;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        arr[temp]++;
    }
    for (int i = n; i>=0; i--) {
        if (arr[i] == i) {
            printf("%d",i);
            return 0;
        }
    }
    printf("-1");
    return 0;
}