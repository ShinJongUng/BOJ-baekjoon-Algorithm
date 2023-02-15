import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
cnt = 0
def BFS(x, y):
    global cnt
    q = deque()
    inside_visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    q.append([y, x])

    while q:
        y, x = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] > graph[y][x]:
                return
            elif graph[ny][nx] == graph[y][x] and not inside_visited[ny][nx]:
                q.append([ny, nx])
                visited[ny][nx] = 1
                inside_visited[ny][nx] = 1
    cnt += 1

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            BFS(j, i)
print(cnt)