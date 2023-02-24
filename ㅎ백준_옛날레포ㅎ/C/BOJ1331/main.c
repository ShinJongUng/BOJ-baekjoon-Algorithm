#include <stdio.h>
#include <string.h>
 
int isValid = 0, visited[6][6] = {0};
int pointx[8] = { -2, -2, -1, -1, 1, 1, 2, 2 }, pointy[8] = { -1, 1, -2, 2, -2, 2, -1, 1 };
int startX, startY, curX, curY, nextX, nextY, toX, toY;
int main() {
    char str[100];
    gets(str);
    startX = 5 - (str[1] - '1');
    startY = str[0] - 'A';
    curX = startX;
    curY = startY;
    visited[curX][curY] = 1;
 
    for (int i = 1; i < 36; i++) {
        gets(str);
        toX = 5 - (str[1] - '1');
        toY = str[0] - 'A';
        
        isValid = 0;
        for (int j = 0; j < 8; j++){
            nextX = curX + pointx[j];
            nextY = curY + pointy[j];
            if (nextX < 0 || nextX >= 6 || nextY < 0 || nextY >= 6)
                continue;
            
            if (nextX == toX && nextY == toY && !visited[nextX][nextY]) {
                visited[nextX][nextY] = 1;
                curX = nextX;
                curY = nextY;
                isValid = 1;
                break;
            }
        }
        if (!isValid) {
            printf("Invalid");
            return 0;
        }
    }
 
    for (int i = 0; i < 8; i++){
        nextX = curX + pointx[i];
        nextY = curY + pointy[i];
        if (nextX < 0 || nextX >= 6 || nextY < 0 || nextY >= 6)
            continue;
 
        if (nextX == startX && nextY == startY) {
            printf("Valid");
            return 0;
        }
    }
 
    printf("Invalid");
}

