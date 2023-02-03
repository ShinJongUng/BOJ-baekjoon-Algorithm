import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    x, a, b = list(map(int, input().split()))
    if not x:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
