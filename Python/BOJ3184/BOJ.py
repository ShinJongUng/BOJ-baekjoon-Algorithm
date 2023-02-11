import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
r, c = list(map(int, input().split()))
visited = [[False] * c for _ in range(r)]
graph = []
wolf_cnt = 0
sheep_cnt = 0

for i in range(r):
    graph.append(list(input().rstrip()))

def BFS(y, x):
    global wolf_cnt, sheep_cnt
    q = deque()
    visited[y][x] = True
    q.append([y, x])
    wolf = 0
    sheep = 0
    if graph[y][x] == 'v':
        wolf += 1
    elif graph[y][x] == 'o':
        sheep += 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if not visited[ny][nx] and graph[ny][nx] != '#':
                if graph[ny][nx] == 'v':
                    wolf += 1
                elif graph[ny][nx] == 'o':
                    sheep += 1
                visited[ny][nx] = True
                q.append([ny, nx])

    if wolf < sheep:
        sheep_cnt += sheep
    else:
        wolf_cnt += wolf


for i in range(r):
    for j in range(c):
        if graph[i][j] != '#' and not visited[i][j]:
            BFS(i, j)

print(sheep_cnt, wolf_cnt)