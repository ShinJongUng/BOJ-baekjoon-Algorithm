import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a



for _ in range(m):
    a, b = list(map(int, input().split()))
    union(a, b)

A = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    if find(A[i]) != find(A[i + 1]):
        cnt += 1

print(cnt)