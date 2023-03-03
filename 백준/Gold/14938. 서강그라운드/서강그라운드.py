import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split()) #지역, 수색범위, 길
graph = [[] for _ in range(n + 1)]
items = [0] + list(map(int, input().split()))
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
ans = 0
for i in range(1, n + 1):
    heap = []
    heapq.heappush(heap, (0, i)) #cost, num
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[i] = 0
    while heap:
        cost, num = heapq.heappop(heap)

        if cost > distance[num]:
            continue

        for nnum, ncost in graph[num]:
            if distance[nnum] > cost + ncost:
                distance[nnum] = cost + ncost
                heapq.heappush(heap, (cost+ncost, nnum))
    temp = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            temp += items[i]
    ans = max(ans, temp)
print(ans)