import sys
input = sys.stdin.readline
t = int(input())
parent = []
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for case in range(t):
    n = int(input())
    parent = [i for i in range(n+1)]
    k = int(input())
    for i in range(k):
        a, b = list(map(int, input().split()))
        union(a, b)
    for i in range(n + 1):
        if i != 0:
            find(i)
    print(f"Scenario {case + 1}:")
    m = int(input())
    for i in range(m):
        u, v = list(map(int, input().split()))
        print(1 if parent[u] == parent[v] else 0)
    print()