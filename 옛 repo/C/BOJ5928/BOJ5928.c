#include <stdio.h>

int main() {
	int D, H, M;
	scanf_s("%d %d %d", &D, &H, &M);
	int time1 = 11 * 60 * 24 + 11 * 60 + 11;
	int time2 = D * 60 * 24 + H * 60 + M;

	int result = time2 - time1;

	printf("%d", result < 0 ? -1 : result);
}