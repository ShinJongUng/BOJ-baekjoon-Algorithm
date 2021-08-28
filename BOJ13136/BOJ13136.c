#include <stdio.h>

int r,c,n;
int main(){
    scanf("%d%d%d", &r, &c, &n);
    
    printf("%lld", (long long)(r/n+(r%n>0?1:0))*(c/n+(c%n>0?1:0)));   
}
