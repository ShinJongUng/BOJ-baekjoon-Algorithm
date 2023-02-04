#include <stdio.h>

int main(void) {
  long long int p1, q1, p2, q2;
  scanf("%lld %lld %lld %lld", &p1,&q1, &p2, &q2);
  printf("%d", (p1 * p2 % (q1 * q2 * 2) == 0)? 1 : 0);
}