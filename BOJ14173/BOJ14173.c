#include <stdio.h>

int max(int a, int b){
  if(a>=b){
    return a;
  }
  else{
    return b;
  }
}

int min(int a, int b){
  if(a<b){
    return a;
  }
  else{
    return b;
  }
}
int main(void) {
  int x1, y1, x2, y2;
  int x3, y3, x4, y4;
  scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
  scanf("%d %d %d %d", &x3, &y3, &x4, &y4);

  int X = max(x2, x4) - min(x1, x3);
  int Y = max(y2, y4) - min(y1, y3);
  int A = max(X,Y);

  printf("%d", A * A);
  return 0;
}