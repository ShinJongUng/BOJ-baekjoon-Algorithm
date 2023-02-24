import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
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

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(n):
         if line[j]:
             union(i, j + 1)

travel = list(map(int,input().split()))

for i in range(len(travel) - 1):
    if find(travel[i]) != find(travel[i + 1]):
        print("NO")
        exit(0)
print("YES")