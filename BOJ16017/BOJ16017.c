#include<stdio.h>

int main() {
	int arr[4];
	for (int a = 0; a < 4; a++) {
		scanf("%d", &arr[a]);
	}
	if (arr[0] > 7 && arr[1] == arr[2] && arr[3] > 7) printf("ignore\n");
	else printf("answer\n");
	return 0;
}