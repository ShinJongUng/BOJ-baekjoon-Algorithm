import sys
from collections import deque
input = sys.stdin.readline

graph = list(list(input().rstrip()) for _ in range(12))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
def Gravity():
    for c in range(6):
        q = deque([])
        for r in range(11, -1, -1):
            if graph[r][c] != '.':
                q.append(graph[r][c])

        for r in range(len(q)):
            graph[11-r][c] = q[r]
        for r in range(12-len(q)):
            graph[r][c] = '.'
    return

def BFS(word, y, x):
    global ans
    q = deque()
    visited = set()
    q.append((y, x))
    visited.add((y, x))
    cnt = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if nx < 0 or ny < 0 or nx >= 6 or ny >= 12:
                continue
            if (ny, nx) not in visited and graph[ny][nx] == word:
                cnt += 1
                q.append([ny, nx])
                visited.add((ny, nx))
    if cnt >= 4:
        for py, px in visited:
            graph[py][px] = '.'
        return True
    return False

Gravity()
f = True
while f:
    f = False
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] != '.':
                flag = BFS(graph[i][j], i, j)
                if flag:
                    f = True
    if f:
        Gravity()
        ans += 1



print(ans)