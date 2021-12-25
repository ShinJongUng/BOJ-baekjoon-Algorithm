#include <stdio.h>

int count(int n, int i) {
    int cnt = 0;
    while(n) {
        if(n % i == 0){
            cnt++;
        }
        else {
            break;
        }
        n /= i;
    }
    return cnt;
}

int main(){
    int t, n;
    scanf("%d",&t);
    while(t--){
        scanf("%d", &n);
        int ans = 0;
        for(int i = 2; i <= 1000; i++) ans += count(n, i);
        printf("%d\n", ans);
    }
}
