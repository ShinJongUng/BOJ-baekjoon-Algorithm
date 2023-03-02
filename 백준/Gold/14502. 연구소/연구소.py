from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
walls = []
safe_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((i, j))
            safe_area += 1
        elif graph[i][j] == 2:
            virus.append((i, j))

def bfs(graph):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

answer = 0
for i in range(len(walls)):
    for j in range(i+1, len(walls)):
        for k in range(j+1, len(walls)):
            wx1, wy1 = walls[i]
            wx2, wy2 = walls[j]
            wx3, wy3 = walls[k]
            if graph[wx1][wy1] == 0 and graph[wx2][wy2] == 0 and graph[wx3][wy3] == 0:
                graph[wx1][wy1] = 1
                graph[wx2][wy2] = 1
                graph[wx3][wy3] = 1
                temp = [row[:] for row in graph]
                bfs(temp)
                cnt = sum(row.count(0) for row in temp)
                answer = max(answer, cnt)
                graph[wx1][wy1] = 0
                graph[wx2][wy2] = 0
                graph[wx3][wy3] = 0

print(answer)