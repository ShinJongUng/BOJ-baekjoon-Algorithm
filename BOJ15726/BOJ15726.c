#include <stdio.h>
#define max(X,Y) ((X) > (Y) ? (X) : (Y))

int main(void) {
  double a,b,c;
  scanf("%lf %lf %lf", &a, &b, &c);

  double num1 = a * b / c;
  double num2 = a / b * c;

  printf("%lld", (long long int)max(num1,num2));
}