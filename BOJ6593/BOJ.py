from collections import deque

xArr = [-1,0,1,0,0,0]
yArr = [0,1,0,-1,0,0]
zArr = [0,0,0,0,1,-1]


def bfs(z1,x1,y1):
    ans=deque()
    ans.append([z1,x1,y1])
    ch[z1][x1][y1] = 0

    while ans:
        z, x, y = ans.popleft()

        for i in range(6):
            nx = x + xArr[i]
            ny = y + yArr[i]
            nz = z + zArr[i] 
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if a[nz][nx][ny] == 'E':
                    print('Escaped in', ch[z][x][y] + 1 ,'minute(s).')
                    return 
                if ch[nz][nx][ny] == -1 and a[nz][nx][ny] == '.':
                    ch[nz][nx][ny]= ch[z][x][y] + 1
                    ans.append([nz,nx,ny])           
    print('Trapped!')
while True:
    l,r,c=map(int,input().split())
    if l == 0 and r == 0 and c == 0:
        break
    a=[[[]*c for i in range(r)] for j in range(l)]
    ch=[[[-1]*c for i in range(r)] for j in range(l)]

    for i in range(l):
        a[i]=[list(input()) for i in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if a[i][j][k] == 'S':
                    bfs(i,j,k)