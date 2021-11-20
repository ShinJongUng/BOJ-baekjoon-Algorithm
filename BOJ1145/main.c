#include <stdio.h>

int input[5];
int main(void) {

for (int i = 0; i < 5; i++)
    scanf("%d", &input[i]);

int num = 1;
while (1){
    int cnt = 0;
    for (int i = 0; i < 5; i++)
        if (num >= input[i] && num % input[i] == 0)
            cnt++;
    if (cnt >= 3){
        printf("%d", num);
        break;
    }
    num++;
}
  
return 0;
}
