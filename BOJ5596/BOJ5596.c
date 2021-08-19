#include <stdio.h>

int max(int A, int B) {
	if (A <= B) {
		return B;
	}
	else {
		return A;
	}
}


int main(void)
{
	int A[5] = { 0 }, B[5] = { 0 };
	int Minguk = 0, Mansae = 0;
	for (int i = 0; i < 4; i++) {
		scanf("%d", &A[i]);
		Minguk += A[i];
	}
	for (int i = 0; i < 4; i++) {
		scanf("%d", &B[i]);
		Mansae += B[i];
	}
	
	printf("%d", max(Minguk, Mansae));
	return 0;
}


