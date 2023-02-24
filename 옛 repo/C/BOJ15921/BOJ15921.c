#include <stdio.h>

int main(void) {
  int n;
  scanf("%d", &n);
  printf("%s", n == 0 ? "divide by zero" : "1.00");
}