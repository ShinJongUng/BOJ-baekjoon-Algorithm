import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

ans = sys.maxsize


for i in range(1, n + 1):
    heap = []
    distance = [sys.maxsize for _ in range(n + 1)]
    heapq.heappush(heap, (0, i))

    while heap:
        cost, num = heapq.heappop(heap)
        if cost != 0 and num == i:
            ans = min(ans, cost)

        if distance[num] < cost:
            continue

        for nnum, ncost in graph[num]:
            if distance[nnum] > ncost + cost:
                distance[nnum] = ncost + cost
                heapq.heappush(heap, (ncost + cost, nnum))

print(ans if sys.maxsize != ans else -1)