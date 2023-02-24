import heapq
import sys
input = sys.stdin.readline

n, e = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)

for i in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a].append([c, b])
    graph[b].append([c, a])

def dijkstra(start):
    hq = []
    heapq.heappush(hq, [0, start])
    distance[start] = 0
    while hq:
        w, x = heapq.heappop(hq)
        if distance[x] < w:
            continue

        for nw, nx in graph[x]:
            cost = nw + w
            if distance[nx] > cost:
                heapq.heappush(hq, (cost, nx))
                distance[nx] = cost

v1, v2 = map(int, input().split())

dijkstra(1)
dist1 = distance[v1]
dist4 = distance[v2]

distance = [sys.maxsize for _ in range(n + 1)]
dijkstra(v1)
dist2 = distance[v2]
dist5 = distance[n]

distance = [sys.maxsize for _ in range(n + 1)]
dijkstra(v2)
dist3 = distance[n]

dist = min(dist1 + dist2 + dist3, dist4 + dist2 + dist5)
print(dist if sys.maxsize > dist else -1)