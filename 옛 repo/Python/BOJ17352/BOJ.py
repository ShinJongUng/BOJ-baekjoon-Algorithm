import sys
input = sys.stdin.readline
n = int(input())
ans = []
bridge = [i for i in range(n + 1)]
def find(x):
    if bridge[x] != x:
        bridge[x] = find(bridge[x])
    return bridge[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        bridge[b] = a
    else:
        bridge[a] = b

for _ in range(n-2):
    a, b = list(map(int, input().split()))
    union(a, b)

for i in range(n + 1):
    if i != 0:
        find(i)

for i in bridge:
    if i == 0:
        continue
    if i not in ans:
        ans.append(i)

print(*ans)
