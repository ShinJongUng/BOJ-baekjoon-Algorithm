import sys
from collections import deque
input = sys.stdin.readline
n, m = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

q = deque()

maxArea = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            cnt += 1
            q.append([i, j])
            visited[i][j] = 1
            area = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if graph[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        area += 1
                        q.append([nx, ny])
            maxArea = max(area, maxArea)

print(cnt)
print(maxArea)