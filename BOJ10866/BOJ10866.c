#include <stdio.h>
#include <stdlib.h>
int main(){
    int queue[20002] = {0,};
    char cmd[11];
    short n;
    scanf("%hd", &n);
    int left = 10000;
    int right = 10001;
    for (int i = 0; i < n; i++) {
        scanf("%s", cmd);
        if (cmd[1] == 'u' && cmd[5] == 'f') {
            scanf("%d", &queue[left--]);
        }
        if (cmd[1] == 'u' && cmd[5] == 'b') {
            scanf("%d", &queue[right++]);
        }
        if (cmd[1] == 'o' && cmd[4] == 'f') {
            if (left == right - 1) {
                printf("-1\n");
            }
            else {
                printf("%d\n", queue[++left]);
                queue[left] = 0;
            }
        }
        if (cmd[1] == 'o' && cmd[4] == 'b') {
            if (left == right - 1) {
                printf("-1\n");
            }
            else {
                printf("%d\n", queue[--right]);
                queue[right] = 0;
            }
        }

        if (cmd[1] == 'i') {
            printf("%d\n", right - left - 1);
        }
        if (cmd[1] == 'm') {
            if (left == right - 1) {
                printf("1\n");
            }
            else printf("0\n");
        }
        if (cmd[1] == 'r') {
            if (left == right - 1) {
                printf("-1\n");
            }
            else printf("%d\n", queue[left + 1]);
        }
        if (cmd[1] == 'a') {
            if (left == right - 1) {
                printf("-1\n");
            }
            else printf("%d\n", queue[right - 1]);
        }
    }
    return 0;
}