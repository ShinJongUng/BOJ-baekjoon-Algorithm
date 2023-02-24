#include <stdio.h>
 
int array[4]={0,1,2,3};
void swap(int x, int y);


int main(){
    
    int M;
    scanf("%d",&M);
    
    for(int i=0;i<M;i++){
        int x,y;
        scanf("%d %d",&x,&y);
        swap(x,y);
    }
    
    for(int i=1;i<=3;i++){
        if(array[i]==1)
            printf("%d",i);
    }
    return 0;
}


void swap(int x, int y){
    int temp=array[x];
    array[x]=array[y];
    array[y]=temp;
    return;
}
