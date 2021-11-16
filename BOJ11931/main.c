#include <stdio.h>
 
int arr[2000002] = { 0, };
 
int main()
{
    int n, i, tmp;
 
    scanf("%d", &n);
 
    for (i = 0; i < n; i++)
    {
        scanf("%d", &tmp);
        arr[tmp+1000000] = 1;
    }
 
    for (i = 2000001; i >= 0; i--)
    {
        if (arr[i] == 1)
            printf("%d\n", i-1000000);
    }
 
    return 0;
}


