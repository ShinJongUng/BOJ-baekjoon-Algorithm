#include <stdio.h>

int main(void) {
  int a1, a2, a3;
  scanf("%d %d %d", &a1, &a2, &a3);
  int b1, b2, b3;
  scanf("%d %d %d", &b1, &b2, &b3);

  int result = 0;  
  if(a1 < b1){
    result += b1 - a1;
  }
  if(a2 < b2){
    result += b2 - a2;
  }
  if(a3 < b3){
    result += b3 - a3;
  }

  printf("%d", result);
}