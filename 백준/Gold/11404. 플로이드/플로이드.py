import sys
INF = 100001
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[sys.maxsize] * n for _ in range(n)]

for i in range(m):
    startCity, arriveCity, cost = map(int, input().split())
    graph[startCity - 1][arriveCity - 1] = min(graph[startCity - 1][arriveCity - 1], cost)

for i in range(n):
    graph[i][i] = 0

    for j in range(n):
        for k in range(n):
            originalRouteCost = graph[j][k] #그냥 가는거
            wayPointRouteCost = graph[j][i] + graph[i][k] #한칸 거쳐서
            graph[j][k] = min(originalRouteCost, wayPointRouteCost)

for i in range(n):
    for j in range(n):
        if graph[i][j] == sys.maxsize:
            print('0', end=" ")
        else:
            print(graph[i][j], end= " ")
    print()