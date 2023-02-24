import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, k = map(int, input().split())
graph = []
time_graph = [[0] * n for _ in range(n)]
idxs = []

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(n):
        if line[j]:
            idxs.append([line[j], i, j, 0])

ss, sx, sy = map(int, input().split())
idxs.sort()
q = deque(idxs)

while q:
    virus, y, x, time = q.popleft()
    if time == ss:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if not graph[ny][nx]:
            graph[ny][nx] = virus
            q.append([virus, ny, nx, time + 1])

print(graph[sx - 1][sy - 1])