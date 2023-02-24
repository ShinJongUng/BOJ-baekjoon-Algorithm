#include <stdio.h>

int main() {
	int day, car[5];
	scanf_s("%d", &day);
	for(int i=0; i<5; i++){
		scanf_s("%d", &car[i]);
	}
	int cnt = 0;
	for (int i = 0; i < 5; i++) {
		if (day == car[i]) {
			cnt++;
		}
	}
	printf("%d", cnt);
}