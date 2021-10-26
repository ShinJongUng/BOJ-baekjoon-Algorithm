#include<stdio.h>
#include<stdlib.h>
#define max(a, b) (((a) > (b)) ? (a) : (b))
int main(){
  int bx, by;
	int dx, dy;
	int jx, jy;
	int countB;
	int countD;
  scanf("%d %d",&bx, &by);
  scanf("%d %d",&dx, &dy);
  scanf("%d %d",&jx, &jy);
 
	countB = max(abs(jx - bx), abs(jy - by));
	countD = abs(jx - dx) + abs(jy - dy);
 
	if (countB < countD) {
		printf("bessie");
	}
	else if (countB > countD) {
		printf("daisy");
	}
	else {
    printf("tie");
	}
 
	return 0;
}