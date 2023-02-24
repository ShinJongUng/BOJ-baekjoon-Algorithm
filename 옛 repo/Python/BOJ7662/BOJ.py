import sys
import heapq
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    visited = [0] * (K + 1)
    heap1, heap2 = [], []
    for j in range(K):
        N = list(map(str, input().strip().split()))
        if N[0] == 'I':
            heapq.heappush(heap1, [int(N[1]), j])
            heapq.heappush(heap2, [int(N[1]) * -1, j])
            visited[j] = 1
        elif N[0] == 'D':
            if N[1] == '-1':
                while heap1 and not visited[heap1[0][1]]:
                    heapq.heappop(heap1)
                if heap1:
                    visited[heap1[0][1]] = 0
                    heapq.heappop(heap1)
            else:
                while heap2 and not visited[heap2[0][1]]:
                    heapq.heappop(heap2)
                if heap2:
                    visited[heap2[0][1]] = 0
                    heapq.heappop(heap2)
    while heap1 and not visited[heap1[0][1]]:
        heapq.heappop(heap1)
    while heap2 and not visited[heap2[0][1]]:
        heapq.heappop(heap2)
    if not heap1:
        print("EMPTY")
    else:
        print(heapq.heappop(heap2)[0] * -1, heapq.heappop(heap1)[0])