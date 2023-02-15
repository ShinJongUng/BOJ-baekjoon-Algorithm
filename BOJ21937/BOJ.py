import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N, M = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = list(map(int, input().split()))
    graph[b].append(a)

cnt = 0
def DFS(idx):
    global cnt
    cnt += 1
    visited[idx] = 1

    for i in graph[idx]:
        if not visited[i]:
            DFS(i)

DFS(int(input()))

print(cnt - 1)