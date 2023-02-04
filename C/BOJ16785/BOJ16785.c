#include <stdio.h>
int main(void)
{
	int a,b,c,i,k=0;
	scanf("%d %d %d",&a,&b,&c);
	for(i=1;k<c;++i)
	{
		k+=a;
		if(i%7==0) k+=b;
	}
	printf("%d",i-1);
	return 0;
}