n = int(input())
p1, p2 = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
def DFS(idx, prev):
    global cnt, p2
    visited[idx] = visited[prev] + 1
    if(idx == p2):
        return
    for i in graph[idx]:
        if not visited[i]:
            DFS(i, idx)

DFS(p1, 0)
print(visited[p2] - 1)