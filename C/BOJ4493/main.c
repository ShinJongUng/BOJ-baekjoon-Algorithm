#include <stdio.h>

int main(){
	int t,n;
	scanf("%d", &t);
	for(int i=0; i<t; i++){
		scanf(" %d", &n);
		int P1 = 0, P2 = 0;
		for(int j=0; j<n; j++){
			char R = 0,S = 0;
			scanf(" %c %c", &R, &S);
			if(R == S){
				P1++;
        P2++;
			}
			else if(R == 'R' && S == 'P'){
	      P2++;
      }
			else if(R == 'R' && S == 'S'){
        P1++;
      }
			else if(R == 'P' && S == 'R'){
        P1++;
      }
			else if(R == 'P' && S == 'S'){
        P2++;
      }
			else if(R == 'S' && S == 'P'){
        P1++;
      }
			else if(R == 'S' && S == 'R'){
        P2++;
      }
		}
    if(P1 == P2)
			printf("TIE\n");
		else if(P1> P2){
			printf("Player 1\n");
		}
		else{
			printf("Player 2\n");
        }
	}
}