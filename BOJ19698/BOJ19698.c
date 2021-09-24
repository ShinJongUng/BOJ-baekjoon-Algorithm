#include <stdio.h>

int min(int A, int B){
  if(A>B){
    return B;
  }
  else{
    return A;
  }
}

int main(void) {
  int N, W, H, L;
  scanf("%d %d %d %d", &N, &W, &H, &L);
  int result = min((W/L)*(H/L),N);
  printf("%d", result);
}