import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

def bfs(start, end):
    q = deque()
    visited = [0] * (n+1)
    q.append(start)
    visited[start] = 1
    while q:
        idx = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[idx] + 1
                if i == end:
                    return visited[i] - 1
    return visited[end] - 1

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


bacon_idx = m
kevin_bacon = sys.maxsize

for i in range(1, n + 1):
    n_kevin_bacon = 0
    for j in range(1, n + 1):
        if i != j:
            n_kevin_bacon += bfs(i, j)
    if kevin_bacon > n_kevin_bacon:
        kevin_bacon = n_kevin_bacon
        bacon_idx = i
    elif kevin_bacon == n_kevin_bacon:
        if bacon_idx > i:
            bacon_idx = i

print(bacon_idx)