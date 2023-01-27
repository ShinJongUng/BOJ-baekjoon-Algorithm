import sys
import heapq
input = sys.stdin.readline
N = int(input())

heap = list(map(int, input().split()))

for i in range(1, N):
    for j in list(map(int, input().split())):
        heapq.heappush(heap, j)
        heapq.heappop(heap)

print(heapq.heappop(heap))