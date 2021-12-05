#include <stdio.h>

int main(void)
{
  int MAX = 3;
	int oneCnt = 0, twoCnt = 0;

	for (int i = 0; i < MAX; i++)
	{
		int num;
		scanf("%d", &num);

		num == 1 ? oneCnt++ : twoCnt++;
	}

	printf(oneCnt > twoCnt ? "1\n" : "2\n");

	return 0;
}