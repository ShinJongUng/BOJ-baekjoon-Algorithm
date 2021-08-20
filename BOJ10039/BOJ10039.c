# include <stdio.h>
int main(void)
{
	int num[5];
	int total = 0;

	for (int i = 0; i < 5; i++)
	{
		scanf_s("%d", &num[i]);
		if (num[i] < 40)
		{
			num[i] = 40;
		}
		total += num[i];
	}
	printf("%d", total / 5);
}