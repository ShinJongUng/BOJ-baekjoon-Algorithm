import sys

input = sys.stdin.readline

M = int(input())
square = []
flag = True
for i in range(M):
    square.append(list(map(int, input().split())))
    for j in range(M):
        if square[i][j] != square[0][0]:
            flag = False

minus_paper = 0
zero_paper = 0
plus_paper = 0

if flag:
    if square[0][0] == -1:
        print("1\n0\n0")
    elif square[0][0] == 0:
        print("0\n1\n0")
    elif square[0][0] == 1:
        print("0\n0\n1")
    exit(0)

def ColorPaper(sx, sy, ex, ey, N):
    global minus_paper, zero_paper, plus_paper, M
    nx = [[sx, sx + N // 3], [sx + N // 3, sx + (N // 3) * 2], [sx + (N // 3) * 2, ex]]
    ny = [[sy, sy + N // 3], [sy + N // 3, sy + (N // 3) * 2], [sy + (N // 3) * 2, ey]]
    for i in range(3):
        for j in range(3):
            mp, zp, pp = 0, 0, 0
            for a in range(ny[i][0], ny[i][1]):
                for b in range(nx[j][0], nx[j][1]):
                    if square[a][b] == 0:
                        zp += 1
                    elif square[a][b] == 1:
                        pp += 1
                    elif square[a][b] == -1:
                        mp += 1
            if zp == (N ** 2) / 9:
                zero_paper += 1
            elif mp == (N ** 2) / 9:
                minus_paper += 1
            elif pp == (N ** 2) / 9:
                plus_paper += 1
            else:
                ColorPaper(nx[j][0], ny[i][0], nx[j][1], ny[i][1], N//3)

ColorPaper(0, 0, M, M, M)

print(minus_paper)
print(zero_paper)
print(plus_paper)