import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

d = [[0] * n for i in range(n)]
for i in range(1, n + 1):
    heap = []
    distance = [sys.maxsize for _ in range(n + 1)]
    heapq.heappush(heap, (0, i))

    while heap:
        cost, num = heapq.heappop(heap)
        if distance[num] < cost:
            continue

        for nnum, ncost in graph[num]:
            if distance[nnum] > ncost + cost:
                distance[nnum] = ncost + cost
                d[nnum - 1][i - 1] = num
                heapq.heappush(heap, (ncost + cost, nnum))

for i in range(n):
    for j in range(n):
        if i == j:
            print('-', end=' ')
        else:
            print(d[i][j], end=' ')
    print()