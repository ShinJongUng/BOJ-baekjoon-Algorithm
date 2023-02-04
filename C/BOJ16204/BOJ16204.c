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
  int N, M, K;
  scanf("%d %d %d", &N, &M, &K);
  printf("%d", min(M, K)+min(N-M, N-K));
}