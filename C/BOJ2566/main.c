#include <stdio.h>

int main() {
    int arr[11][11] = {0};
    int max = 0, maxi=0, maxj=0;
    for(int i =1; i<=9; i++){
        for(int j=1; j<=9; j++){
            scanf("%d", &arr[i][j]);
            if(max<arr[i][j]){
                max = arr[i][j];
                maxi = i;
                maxj = j;
            }
        }
    }
    
    printf("%d\n%d %d", max, maxi, maxj);
    return 0;
}
