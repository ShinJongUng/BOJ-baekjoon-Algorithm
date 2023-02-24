#include <stdio.h>

int main(void) {
  int n, m;
  scanf("%d %d", &n, &m);
  if(m==1||m==2) printf("NEWBIE!");
    else if(2 < m && m <= n) printf("OLDBIE!");
    else printf("TLE!");
}