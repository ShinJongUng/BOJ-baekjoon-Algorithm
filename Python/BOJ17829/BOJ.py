import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def pulling(startx, starty, n):
    if n == 2:
        temp = []
        for i in range(startx, startx + n):
            for j in range(starty, starty + n):
                temp.append(board[i][j])
        return sorted(temp)[2]
    else:
        a = pulling(startx, starty, n // 2)
        b = pulling(startx, starty + n // 2, n // 2)
        c = pulling(startx + n // 2, starty, n // 2)
        d = pulling(startx + n // 2, starty + n // 2, n // 2)
        return sorted([a,b,c,d])[2]

print(pulling(0, 0, n))