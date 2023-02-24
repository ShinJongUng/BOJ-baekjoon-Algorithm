import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

light_graph = [[] for _ in range(n + 1)]
heavy_graph = [[] for _ in range(n + 1)]
mid_weight = n // 2 + 1
for i in range(m):
    a, b = map(int, input().split()) # a > b 무게
    light_graph[b].append(a)
    heavy_graph[a].append(b)

cnt = 0
def bfs(start_idx, graph):
    global cnt
    visited = [False] * (n + 1)
    q = deque()
    q.append(start_idx)
    while q:
        num = q.popleft()
        if not visited[num]:
            visited[num] = True
            q.extend(graph[num])

    child_num = visited.count(True)
    if child_num > mid_weight: # 구슬 5개일때 자식이나 손자 3개 이상이면 조건 성립 O
        cnt += 1

for i in range(1, n + 1):
    bfs(i, light_graph)
    bfs(i, heavy_graph)

print(cnt)