import sys
from collections import deque
input = sys.stdin.readline

M, N = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

q = deque()
ans = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            q.append([i, j])
            visited[i][j] = 1
            ans += 1
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        continue
                    if graph[nx][ny] and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = 1

print(ans)