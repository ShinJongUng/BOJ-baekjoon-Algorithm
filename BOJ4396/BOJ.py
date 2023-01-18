import sys
input = sys.stdin.readline

n = int(input())
boom = [list(input().rstrip()) for _ in range(n)]
graph = [list(input().rstrip()) for _ in range(n)]

dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

isMine = False

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'x':
            if boom[i][j] == '.':
                graph[i][j] = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if boom[nx][ny] == '*':
                        graph[i][j] += 1
            else:
                isMine = True

if not isMine:
    for i in range(n):
        print("".join(map(str, graph[i])))
else:
    for i in range(n):
        for j in range(n):
            if boom[i][j] == '*':
                print("*", end='')
            else:
                print(graph[i][j], end='')
        print()