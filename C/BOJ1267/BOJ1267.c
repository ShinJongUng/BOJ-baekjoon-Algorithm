#include <stdio.h> 
int main() {
   int N, arr[21];
   scanf("%d", &N);
   for(int i=0; i<N; i++){
     scanf("%d", &arr[i]);
   }
   
  int Y = 0, M = 0, Y1 = 0, M1 = 0;
  for(int i =0, Y = 0; i<N; i++){
    if(arr[i] > 0){
      
        Y = arr[i] / 30;
        Y +=1;
        Y1 += Y;
    }
  }
  Y1 = Y1 * 10;
  for(int i =0, M = 0; i<N; i++){
    if(arr[i] > 0){
        M = arr[i] / 60;
        M += 1;
        M1 += M;
    }
  }
  M1 = M1 * 15;

  if(M1 < Y1){
    printf("M %d", M1);
  }
  else if( M1 == Y1){
    printf("Y M %d", M1);
  }
  else{
    printf("Y %d", Y1);
  }
}

