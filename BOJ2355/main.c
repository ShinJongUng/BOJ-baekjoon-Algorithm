#include <stdio.h>

int main(int argc, const char * argv[]) {
    long long int a, b;
    scanf("%lld %lld", &a, &b);
    
    if(a<=b){
        printf("%lld", (b-a+1) * (a+b)/2);
    }
    else{
        printf("%lld", (a-b+1) * (a+b)/2);
    }
}
