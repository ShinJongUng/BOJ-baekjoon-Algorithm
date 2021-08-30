#include <stdio.h>


int main()
{

	int a, b;

	scanf("%d %d", &a, &b);

	int lab = 1;
	int cur = a;

	lab += (cur % (b - a) == 0) ? cur / (b - a) : cur / (b - a) + 1;

	printf("%d", lab);

	return 0;
}
