import sys
from collections import deque
input = sys.stdin.readline
N, M, T = list(map(int, input().rstrip().split()))
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))

visited = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
gram = 1000000
def BFS(ix, iy, v):
    global gram
    q = deque()
    q.append([ix, iy])
    visited[ix][iy] = v
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            return min(visited[x][y] - 1, gram)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 2:
                        gram = (N - 1) - nx + (M - 1) - ny + visited[x][y]
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return gram


ans = BFS(0, 0, 1)

if ans <= T:
    print(ans)
else:
    print("Fail")
