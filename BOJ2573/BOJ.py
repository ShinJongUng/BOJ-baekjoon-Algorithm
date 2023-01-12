import sys
from collections import deque
N, M = list(map(int, sys.stdin.readline().rstrip().split()))
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def BFS(ix, iy, visited, endP):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append([ix, iy])
    visited[ix][iy] = 1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif graph[nx][ny] <= 0 and graph[nx][ny] >= endP:
                if graph[x][y] > 0:
                    graph[x][y] -= 1
                    if not graph[x][y]:
                        graph[x][y] = endP - 1

            if graph[nx][ny] > 0:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

ans = 0
AllCnt = 0
for k in range(300):
    visit = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visit[i][j]:
                BFS(i, j, visit, -AllCnt)
                AllCnt += 1
                cnt += 1
    if cnt >= 2:
        ans = k
        break

print(ans)