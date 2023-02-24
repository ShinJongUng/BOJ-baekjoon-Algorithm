#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);
    int arr[101] = { 0 };
    int seat;
    int cnt = 0;
    for (int i = 0;i < N;i++)
    {
        scanf("%d", &seat);
        if (arr[seat] == 1)
            cnt++;
        arr[seat] = 1;
    }
    printf("%d", cnt);
}
