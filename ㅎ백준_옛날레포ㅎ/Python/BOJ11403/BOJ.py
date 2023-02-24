import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]



def bfs(x, y):
    visited = [0] * n
    q = deque()
    q.append(x)
    while q:
        idx = q.popleft()
        for i in graph[idx]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                if i == y:
                    return 1

    return 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            graph[i].append(j)
for i in range(n):
    for j in range(n):
        print(bfs(i, j), end=" ")
    print()

