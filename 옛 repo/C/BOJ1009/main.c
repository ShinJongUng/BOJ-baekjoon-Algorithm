#include <stdio.h>
int main()
{
    int n, a, b;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d %d", &a, &b);
        int num = 1;
        for (int j = 0; j < b; j++)
        {
            num *= a; 
            num %= 10;                  
        }
        if (num == 0) 
            printf("10\n");
        else 
            printf("%d\n", num);
    }
}
