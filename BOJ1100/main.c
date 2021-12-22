#include <stdio.h>

char board[8][8];
int sum = 0;

int main(void){
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            scanf(" %c", &board[i][j]);
        }
    }
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if((i+j)%2==0 && board[i][j] == 'F'){
                sum++;
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}
