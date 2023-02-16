import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
for i in range(n):
    x, y = map(int, input().split())
    graph[x] = y
for i in range(m):
    u, v = map(int, input().split())
    graph[u] = v

q = deque()
q.append(1)
visited[1] = 1
while q:
    num = q.popleft()
    if num == 100:
        print(visited[num] - 1)
        break
    for i in range(1, 7):
        if num + i <= 100:
            if graph[num + i]:
                if not visited[graph[num + i]]:
                    q.append(graph[num + i])
                    visited[graph[num + i]] = visited[num] + 1
            else:
                if not visited[num + i]:
                    q.append(num + i)
                    visited[num + i] = visited[num] + 1
