#include <stdio.h>

int main(void) {
  double a, b;
  scanf("%lf %lf", &a, &b);

  printf("%.6lf", a * 2 + b * 3.141592 * 2);
}