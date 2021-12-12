#include <stdio.h>

int main()
{
    int a = 0, arr[1001] = { 0, };
    int b = 0, c;

    for (int i = 0; i < 10; i++) {
        int tmp;
        scanf("%d",&tmp);

        arr[tmp]++;
        a += tmp;
    }

    for (int i = 10; i < 1001; i += 10) {
        if (arr[i] && b < arr[i]) {
            b = arr[i];
            c = i;
        }
    }

    printf("%d\n%d", a / 10, c);
}
