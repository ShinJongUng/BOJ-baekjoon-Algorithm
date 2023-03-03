import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v, cost = map(int, input().split())
    graph[u].append([v, cost])
    graph[v].append([u, cost])

for i in range(m):
    u, v = map(int, input().split())
    visited = [INF for _ in range(n + 1)]

    q = deque()
    q.append(u)
    visited[u] = 0

    while q:
        num = q.popleft()

        for n_num, cost in graph[num]:
            if visited[num] + cost < visited[n_num]:
                visited[n_num] = visited[num] + cost
                q.append(n_num)
    print(visited[v])
