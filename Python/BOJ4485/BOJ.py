import heapq
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 1
while True:
    n = int(input())
    if not n:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[sys.maxsize] * n for _ in range(n)]

    hq = []
    heapq.heappush(hq, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while hq:
        w, x, y = heapq.heappop(hq)

        if distance[x][y] < w:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[nx][ny] > w + graph[nx][ny]:
                heapq.heappush(hq, (w + graph[nx][ny], nx, ny))
                distance[nx][ny] = w + graph[nx][ny]
    print(f"Problem {cnt}:", distance[n-1][n-1])
    cnt += 1

