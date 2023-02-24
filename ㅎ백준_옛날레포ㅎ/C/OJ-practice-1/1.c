#include <stdio.h>

int main(void) {
    int arr[101] ={0};
    int max = 0, n = 0, maxer = 0;
    for(int i = 0; i < 1000; i++){
        scanf("%d", &n);
        arr[n]++;
        if(arr[n] > max)
            max = arr[n];
    }
    
    for(int i = 1; i<= 100; i++){
        if(arr[i] == max){
            if(maxer < i){
                maxer = i;
            }
        }
    }
    
    printf("%d", maxer);
    return 0;
}