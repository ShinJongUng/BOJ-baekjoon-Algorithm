import sys
from collections import deque
import copy
input = sys.stdin.readline

# 4방향 탐색을 위한 dx, dy
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# bfs 함수 정의
def bfs(graph, x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

# 조합을 위한 dfs 함수 정의
def dfs(graph, count):
    global result
    if count == 3:
        temp = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    bfs(temp, i, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1
        result = max(result, count)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(graph, count+1)
                graph[i][j] = 0

# 입력 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 0
dfs(graph, 0)
print(result)