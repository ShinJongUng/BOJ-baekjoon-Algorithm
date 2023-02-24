import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]

K = int(input())

for i in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((c, b))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        w, x = heapq.heappop(hq)
        if distance[x] < w:
            continue
        for nw, nx in graph[x]:
            ndw = w + nw
            if distance[nx] > ndw:
                heapq.heappush(hq, (ndw, nx))
                distance[nx] = ndw

dijkstra(K)

for i in range(1, n + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
