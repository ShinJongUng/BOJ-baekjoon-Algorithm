#include <stdio.h>

int main() {
	long long int n = 5, time = 0, m = 0, s = 7;
	scanf_s("%lld", &m);
	for (time = 2; time <= m; time++) {
		n += s;
		s += 3;
	}
	printf("%lld", n % 45678);
}