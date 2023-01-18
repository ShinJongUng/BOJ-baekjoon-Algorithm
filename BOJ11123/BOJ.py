import sys
from collections import deque
input = sys.stdin.readline
T = int(input())


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for k in range(T):
    H, W = list(map(int, input().rstrip().split()))
    graph = [list(map(str, input().rstrip())) for i in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] != '#' or visited[i][j]:
                continue
            q = deque()
            q.append([i, j])
            visited[i][j] = 1
            cnt += 1
            while q:
                y, x = q.popleft()
                for s in range(4):
                    nx = x + dx[s]
                    ny = y + dy[s]
                    if nx < 0 or nx >= W or ny < 0 or ny >= H:
                        continue
                    if graph[ny][nx] == '#' and not visited[ny][nx]:
                        q.append([ny, nx])
                        visited[ny][nx] = 1
    print(cnt)


