#include <stdio.h>

int main() {

    long long n, sum = 0;
    
    scanf("%lld", &n);

    for (long long i = 1; i < n; i++)
        sum += i * (n + 1);


	printf("%lld", sum);
}