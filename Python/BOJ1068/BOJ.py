import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())

visited = [False] * n
graph = dict()
cnt = 0
arr = list(map(int, input().split()))
removenode = int(input())
def DFS(idx):
    global cnt, removenode
    visited[idx] = True
    isLeaf = True
    if idx in graph:
        if (len(graph[idx]) == 1 and removenode == graph[idx][0]) or (len(graph[idx]) == 2 and sorted(graph[idx]) == sorted([removenode, idx])):
            cnt += 1
            return
        for i in graph[idx]:
            if i == removenode:
                isLeaf = False
                continue
            if i != idx and not visited[i]:
                isLeaf = False
                DFS(i)
    if isLeaf:
        cnt += 1

rootnode = []

for i in range(len(arr)):
    if arr[i] == -1:
        rootnode.append(i)
        if i not in graph:
            graph[i] = [i]
        else:
            graph[i].append(i)
        continue
    if arr[i] not in graph:
        graph[arr[i]] = [i]
    else:
        graph[arr[i]].append(i)

for i in rootnode:
    if i != removenode:
        DFS(i)
print(cnt)