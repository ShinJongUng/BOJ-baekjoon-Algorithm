from collections import deque
R, C, N = list(map(int, input().split()))
graph = []
for _ in range(R):
    graph.append(list(map(str, input())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x, y])
    graph[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            else:
                if graph[nx][ny] == 'O':
                    q.append([nx, ny])
                graph[nx][ny] = 1


def ans():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                bfs(i, j)

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1:
                graph[i][j] = '.'
            else:
                graph[i][j] = 'O'

if N % 2 == 0:
    tmp = ['O'] * C
    for _ in range(R):
        print("".join(map(str, tmp)))
elif N > 1 and N % 4 == 1:
    ans()
    ans()
    for i in graph:
        print("".join(map(str, i)))
elif N % 4 == 3:
    ans()
    for i in graph:
        print("".join(map(str, i)))
else:
    for i in graph:
        print("".join(map(str, i)))




