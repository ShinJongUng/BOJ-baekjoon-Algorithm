import sys
input = sys.stdin.readline
N, M = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * N
def dfs(idx, depth):
    visited[idx] = 1
    if depth == 4:
        print(1)
        exit(0)
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0



for i in range(N):
    dfs(i, 0)
    visited[i] = 0

print(0)