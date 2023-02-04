import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [0] * (N)

q = deque()
q.append(0)
visited[0] = 1
while q:
    idx = q.popleft()
    for i in graph[idx]:
        if not visited[i]:
            q.append(i)
            visited[i] = visited[idx] + 1

distance = max(visited)
number = visited.index(distance)
cnt = visited.count(distance)
print(number+1, distance - 1, cnt)
