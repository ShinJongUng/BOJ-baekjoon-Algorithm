import sys
input = sys.stdin.readline

n = int(input())
quad = [list(input().rstrip()) for _ in range(n)]
ans = []
def zip(startx, starty, size):
    check = quad[startx][starty]
    flag = True
    if size != 1:
        for i in range(startx, startx + size):
            for j in range(starty, starty + size):
                if check != quad[i][j]:
                    flag = False
                    break
    else:
        ans.append(check)
        return
    if flag:
        ans.append(check)
    else:
        ans.append('(')
        size //= 2
        zip(startx, starty, size)
        zip(startx, starty + size, size)
        zip(startx + size, starty, size)
        zip(startx + size, starty + size, size)
        ans.append(')')

zip(0, 0, n)

print("".join(ans))