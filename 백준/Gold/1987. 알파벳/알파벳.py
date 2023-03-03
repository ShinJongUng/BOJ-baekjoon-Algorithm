import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
words_set = set()
graph = [list(input().rstrip()) for _ in range(n)]
ans = 0
def DFS(y, x, distance):
    global ans
    ans = max(ans, distance)
    words_set.add(graph[y][x])
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[ny][nx] not in words_set:
            DFS(ny, nx, distance + 1)
    words_set.remove(graph[y][x])

DFS(0, 0, 1)

print(ans)