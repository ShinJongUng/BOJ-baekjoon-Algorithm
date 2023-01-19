import sys
from collections import deque
input = sys.stdin.readline
n, m, k = list(map(int, input().split()))

graph = [[0] * n for _ in range(m)]

for i in range(k):
    sx, sy, ex, ey = list(map(int, input().split()))

    for j in range(sy, ey):
        for s in range(sx, ex):
            graph[s][j] = 1

visited = [[0] * n for _ in range(m)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

ans = []
q = deque()
for i in range(m):
    for j in range(n):
        if not graph[i][j] and not visited[i][j]:
            q.append([i,j])
            visited[i][j] = 1
            cnt = 1
            while q:
                x, y = q.popleft()
                for s in range(4):
                    nx = x + dx[s]
                    ny = y + dy[s]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if not graph[nx][ny] and not visited[nx][ny]:
                        q.append([nx, ny])
                        cnt += 1
                        visited[nx][ny] = 1
            ans.append(cnt)

print(len(ans))
print(*list(sorted(ans)))