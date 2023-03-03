import sys
import heapq
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

heap = []
heapq.heappush(heap, [0, 0, 0])
visited[0][0] = 1

while heap:
    cost, x, y = heapq.heappop(heap)
    if x == n - 1 and y == n - 1:
        print(cost)
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if not visited[nx][ny]:
            if graph[nx][ny] == '0':
                visited[nx][ny] = 1
                heapq.heappush(heap, [cost + 1, nx, ny])
            else:
                visited[nx][ny] = 1
                heapq.heappush(heap, [cost, nx, ny])