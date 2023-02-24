#include <stdio.h>

int main() {
	int A, B;
	scanf_s("%d %d", &A, &B);
	int speed = B - A;
	if (speed <= 0) {
		printf("Congratulations, you are within the speed limit!");
	}
	else {
		if (1 < speed && speed <= 20) {
			printf("You are speeding and your fine is $100.");
		}
		else if (21 < speed && speed <= 30) {
			printf("You are speeding and your fine is $270.");
		}
		else {
			printf("You are speeding and your fine is $500.");
		}
	}

}
