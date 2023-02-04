#include <stdio.h>

int main(){
	
	int N;
	
	while(1){
		scanf("%d", &N);
        int sum=0;
		
		if(N==0)
			return 0;
			
		while(1){
			if(N%10==1) sum+=2;
			else if(N%10==0) sum+=4;
			else sum+=3;	
			
			if(N<10) break;
			
			N/=10;
			sum+=1;	
		}
		
		printf("%d\n", sum+2);
	}
	return 0; 
}