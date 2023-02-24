import sys
from collections import deque
t = int(input())

def BFS(coord):
    q = deque()
    q.append([coord[0][0], coord[0][1]])
    visited = [0 for _ in range(len(coord) - 2)] # 0 1
    while(q):
        x, y = q.popleft()
        if abs(coord[len(coord) - 1][0] - x) + abs(coord[len(coord)- 1][1] - y) <= 1000:
            print("happy")
            return
        for i in range(1, len(coord) - 1): # 1, 2
            if not visited[i - 1]:
                if abs(x - coord[i][0]) + abs(y - coord[i][1]) <= 1000:
                    visited[i - 1] = 1
                    q.append([coord[i][0], coord[i][1]])
    print("sad")



for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    coord = [] # 0: 집, 1~n: 편의점, n+1: 락 페스티벌
    for _ in range(n+2):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        coord.append(line)
    BFS(coord)