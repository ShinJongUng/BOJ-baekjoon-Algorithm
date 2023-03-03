import sys
import heapq
input = sys.stdin.readline

n, m, h1, h2 = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap = []
heapq.heappush(heap, (0, h1)) #순위, 값
distance[h1] = 0

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue
    for ndist, cost in graph[now]:
        if dist + cost < distance[ndist]:
            distance[ndist] = dist + cost
            heapq.heappush(heap, (dist + cost, ndist))

print(distance[h2])