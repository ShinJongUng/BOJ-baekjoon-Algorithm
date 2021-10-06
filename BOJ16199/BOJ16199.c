#include <stdio.h>

int main() {
    int flag = 0;
    int a1, a2, a3;
    int b1, b2, b3;
    scanf("%d %d %d", &a1, &a2, &a3);
    scanf("%d %d %d", &b1, &b2, &b3);
    if (b1 - a1 == 0)
        flag = 0;
    else if (b1 - a1 == 1)
    {
        if (b2 == a2)
        {
            if (b3 >= a3) flag = 1;
            else flag = 0;
        }
        else if (b2 > a2) flag = 1;
        else flag = 0;
    }
    else
    {
        if (b2 == a2)
        {
            if (b3 >= a3) flag = 2;
            else flag = 1;
        }
        else if (b2 > a2) flag = 2;
        else flag = 1;
    }

    if (b1 - a1 < 2)
        printf("%d\n%d\n%d", flag, b1 - a1 + 1, b1 - a1);
    else printf("%d\n%d\n%d", b1 - a1 + flag - 2, b1 - a1 + 1, b1 - a1);
}
