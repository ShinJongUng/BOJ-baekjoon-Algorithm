#include <stdio.h>
#include <stdlib.h>


int main(void) {
	int value[5];

	for (int i = 0; i < 5; i++) {
		scanf("%d", &value[i]);
	}
	if (value[0] < 0) {
		int A = abs(value[0]);
		int C = value[2] * A;
		int E = value[4] * value[1];

		printf("%d", C + E + value[3]);

	}
	else {
		int C = value[1] - value[0];
		printf("%d", C * value[4]);
	}

}
