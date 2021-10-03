#include <stdio.h>
#include <math.h>

int main(void) {
  double a;
  scanf("%lf", &a);

  printf("%.7lf", 4*sqrt(a));
}