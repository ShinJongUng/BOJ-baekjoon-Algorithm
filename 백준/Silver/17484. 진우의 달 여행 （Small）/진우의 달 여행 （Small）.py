import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[[] for _ in range(m)] for _ in range(n)]
for j in range(m):
    if j - 1 >= 0:
        visited[1][j - 1].append([1, graph[0][j] + graph[1][j - 1]]) #direction, value
    if j + 1 < m:
        visited[1][j + 1].append([3, graph[0][j] + graph[1][j + 1]])
    visited[1][j].append([2, graph[0][j] + graph[1][j]])

for i in range(1, n):
    for j in range(m):
        for k in range(len(visited[i][j])):
            di, val = visited[i][j][k]
            if j - 1 >= 0 and i + 1 < n and di != 1:
                visited[i + 1][j - 1].append([1, graph[i + 1][j - 1] + val])
            if j + 1 < m and i + 1 < n and di != 3:
                visited[i + 1][j + 1].append([3, graph[i + 1][j + 1] + val])
            if i + 1 < n and di != 2:
                visited[i + 1][j].append([2, graph[i + 1][j] + val])

ans = sys.maxsize
for i in range(m):
    for di, val in visited[n - 1][i]:
        ans = min(ans, val)

print(ans)