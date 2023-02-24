from collections import deque
n, m, h = list(map(int, input().split()))
graph = []
t_xy = []
for k in range(h):
    temp = []
    for i in range(m):
        line = list(map(int, input().split()))
        for j in range(n):
            if(line[j] == 1):
                t_xy.append([k, i, j])
        temp.append(line)
    graph.append(temp)


def bfs(t_xy):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dh = [-1, 1]
    q = deque()
    visited = [[[0] * n for _ in range(m)]for _ in range(h)]
    maxNum = 1
    if(not t_xy):
        return [visited, 1]
    for index in t_xy:
        q.append(index)
        visited[index[0]][index[1]][index[2]] = 1
    while q:
        n_h, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif graph[n_h][nx][ny] == 1:
                continue
            elif not graph[n_h][nx][ny]:
                if not visited[n_h][nx][ny]:
                    q.append([n_h, nx, ny])
                    visited[n_h][nx][ny] = visited[n_h][x][y] + 1
                    maxNum = max(visited[n_h][nx][ny], maxNum)
        for i in range(2):
            nh = n_h + dh[i]
            if nh < 0 or nh >= h:
                continue
            elif graph[nh][x][y] == 1:
                continue
            elif not graph[nh][x][y]:
                if not visited[nh][x][y]:
                    q.append([nh, x, y])
                    visited[nh][x][y] = visited[n_h][x][y] + 1
                    maxNum = max(visited[nh][x][y], maxNum)
    return [visited, maxNum]

def result(maxNum, visited):
    for k in range(h):
        for i in range(m):
            for j in range(n):
                if(graph[k][i][j] == 0 and visited[k][i][j] == 0):
                    return -1
    return maxNum - 1
b, a = bfs(t_xy)
print(result(a, b))