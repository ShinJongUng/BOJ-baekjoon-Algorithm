import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = list(map(int, input().split()))

graph[r1][c1] = 1
graph[r2][c2] = 2

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque()
q.append([r1, c1])
visited[r1][c1] = 1
while q:
    r, c = q.popleft()
    if r == r2 and c == c2:
        break
    for i in range(6):
        nx = r + dx[i]
        ny = c + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny]:
            q.append([nx, ny])
            visited[nx][ny] = visited[r][c] + 1

print(visited[r2][c2] - 1)

