import sys
input = sys.stdin.readline

M = int(input())
square = []
for _ in range(M):
    square.append(list(map(int, input().split())))

blue_cnt = 0
white_cnt = 0
def ColorPaper(sx, sy, ex, ey, N):
    global blue_cnt, white_cnt, M
    if N == M:
        flag = False
        for i in range(N):
            if flag: break
            for j in range(N):
                if square[0][0] != square[j][i]:
                    flag = True
                    break
        if not flag:
            print("1\n0" if not square[0][0] else "0\n1")
            exit(0)

    nx = [[sx, ex - N//2], [sx, ex - N//2], [ex - N//2, ex], [ex - N//2, ex]]
    ny = [[sy, ey - N//2], [ey - N//2, ey], [sy, ey - N//2], [ey - N//2, ey]]
    for i in range(4):
        b_cnt = 0
        w_cnt = 0
        for j in range(ny[i][0], ny[i][1]):
            for k in range(nx[i][0], nx[i][1]):
                if square[j][k]:
                    b_cnt += 1
                else:
                    w_cnt += 1
        if not b_cnt:
            white_cnt += 1
        elif not w_cnt:
            blue_cnt += 1
        else:
            ColorPaper(nx[i][0], ny[i][0], nx[i][1], ny[i][1], N//2)

ColorPaper(0, 0, M, M, M)

print(white_cnt)
print(blue_cnt)