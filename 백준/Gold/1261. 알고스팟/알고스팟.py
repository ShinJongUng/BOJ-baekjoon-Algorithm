import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[sys.maxsize] * n for _ in range(m)]
q = deque()
visited[0][0] = 0
q.append([0, 0])
while q:
    y,x = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if visited[ny][nx] > visited[y][x] + int(graph[ny][nx]):
            if graph[ny][nx] == '1':
                visited[ny][nx] = visited[y][x] + 1
                q.append([ny, nx])
            else:
                visited[ny][nx] = visited[y][x]
                q.append([ny, nx])

print(visited[m-1][n-1])