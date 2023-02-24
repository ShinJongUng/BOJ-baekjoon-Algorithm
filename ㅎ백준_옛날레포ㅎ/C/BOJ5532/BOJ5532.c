#include <stdio.h>

int max(int day1, int day2) {
	if (day1 >= day2) {
		return day1;
	}
	else {
		return day2;
	}
}

int main(void)
{
	int L, A, B, C, D;
	scanf_s("%d %d %d %d %d", &L, &A, &B, &C, &D);

	int day1, day2;

	day1 = A / C;
	day2 = B / D;

	if (A % C != 0) {
		day1++;
	}
	if (B % D != 0) {
		day2++;
	}

	printf("%d", (L - max(day1, day2)));
}