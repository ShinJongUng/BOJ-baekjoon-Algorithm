from collections import deque
n, m = list(map(int, input().split()))
graph = []
t_xy = []
for i in range(m):
    line = list(map(int, input().split()))
    for j in range(n):
        if(line[j] == 1):
            t_xy.append([i, j])
    graph.append(line)

def bfs(t_xy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    visited = [[0] * n for _ in range(m)]
    maxNum = 1
    if(not t_xy):
        return [visited, 1]
    for index in t_xy:
        q.append(index)
        visited[index[0]][index[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif graph[nx][ny] == 1:
                continue
            elif not graph[nx][ny]:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    maxNum = max(visited[nx][ny], maxNum)

    return [visited, maxNum]

def result(maxNum, visited):
    for i in range(m):
        for j in range(n):
            if(graph[i][j] == 0 and visited[i][j] == 0):
                return -1
    return maxNum - 1
b, a = bfs(t_xy)
print(result(a, b))