import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
parent = [[i, 1] for i in range(1000001)]

def find(x):
    if x != parent[x][0]:
        parent[x][0] = find(parent[x][0])[0]
    return parent[x]

def union(a, b):
    a, a_cnt = find(a)
    b, b_cnt = find(b)
    if a != b:
        parent[a][0] = b
        parent[b][1] += parent[a][1]
        parent[a][1] = 1

for i in range(n):
    line = list(input().rstrip().split())
    if line[0] == 'I':
        union(int(line[1]), int(line[2]))
    elif line[0] == 'Q':
        print(parent[find(int(line[1]))[0]][1])
