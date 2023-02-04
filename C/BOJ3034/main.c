#include <stdio.h>
#include <math.h>

int main(){
    int N, W, H, tmp;
    scanf("%d %d %d", &N, &W, &H);

    int size = pow(W,2) + pow(H,2);
    for(int i = 0; i < N; i++){
        scanf("%d", &tmp);
        if(pow(tmp,2) <= size){
            printf("DA\n");
        }
        else{
            printf("NE\n");
        }
    }
}