#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	int sum = 0, min = 100, tmp;
	for (int i = 0; i < n; i++) {
		min = 100;
		sum = 0;
		for (int j = 0; j < 7; j++) {
			scanf("%d", &tmp);
			if (tmp % 2 == 0) {
				sum += tmp;
				if (min > tmp) {
					min = tmp;
				}
			}
		}
		printf("%d %d\n", sum, min);
	}
}