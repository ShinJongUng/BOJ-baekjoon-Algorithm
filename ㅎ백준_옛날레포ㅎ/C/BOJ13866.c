#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int score[4];

	for (int i = 0; i < 4; i++) {
		scanf("%d", &score[i]);
	}

	printf("%d", abs((score[0] + score[3]) - (score[1] + score[2])));
}