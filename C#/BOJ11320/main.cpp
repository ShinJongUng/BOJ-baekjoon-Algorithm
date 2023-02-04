#include <stdio.h>
int main()
{

    int N;
    scanf("%d", &N);
    double F, S;
    for (int i = 0;i < N;i++)
    {
        scanf("%lf %lf", &F, &S);
        printf("%.0lf\n", (F*F / 2) / (S*S / 2));
    }
}