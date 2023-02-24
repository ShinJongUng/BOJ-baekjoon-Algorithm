#include <stdio.h>
#include <string.h>

int main(){
    int n1, n2, max=0;
    int t[11] = {0};
    
    for(int i = 1; i<= 10; i++){
        scanf("%d %d", &n1, &n2);
        t[i] = t[i-1];
        t[i] -= n1;
        t[i] += n2;
    }
    
    for(int i = 1; i<=10; i++){
        if(max < t[i])
            max = t[i];
    }
    
    printf("%d", max);
}
