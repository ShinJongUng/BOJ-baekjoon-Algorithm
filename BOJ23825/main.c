#include <stdio.h>
#pragma warning (disable:4996)

int min(int a, int b) {
	if (a > b) {
		return b;
	}
	else {
		return a;
	}
}

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", min(a, b) / 2);
}
