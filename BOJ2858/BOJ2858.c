#include <stdio.h>

int main(void){
	int R, B, sum = 0, l = 0 , w=0;
	
	scanf("%d %d", &R, &B);
	sum = R + B;	
	for(l = 2;; l++){
		if(sum % l == 0){
			if((l-2) * (sum / l-2) == B){
				w = sum / l;
				break;
			}
		}
	}
	
	if(w < l)
		printf("%d %d", l, w);
	else
		printf("%d %d", w, l);
	
}
