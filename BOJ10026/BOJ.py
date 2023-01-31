import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

visited = [[False] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
def bfs(x, y, isNormal):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        ix, iy = q.popleft()
        for i in range(4):
            nx = ix + dx[i]
            ny = iy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                if graph[ix][iy] == graph[nx][ny] or (isNormal and ((graph[ix][iy] == 'R' and graph[nx][ny] == 'G') or (graph[ix][iy] == 'G' and graph[nx][ny] == 'R'))):
                    q.append([nx, ny])
                    visited[nx][ny] = True

normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_cnt += 1
            bfs(i, j, False)

not_normal_cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            not_normal_cnt += 1
            bfs(i, j, True)
print(normal_cnt, not_normal_cnt)