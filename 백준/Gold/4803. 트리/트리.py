import sys
input = sys.stdin.readline

parent = []

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

rec = 1
while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    parent = [i for i in range(n + 1)]
    cycle = []
    for i in range(m):
        a, b = map(int, input().split())
        a = find(a)
        b = find(b)
        if a != b:
            union(a, b)
        else:
            cycle.append(a)
    ans_set = set()
    for i in range(1, n + 1):
        ans_set.add(find(i))
    ans = 0
    cycle_set = set()
    for i in cycle:
        cycle_set.add(find(i))

    for i in ans_set:
        if i not in cycle_set:
            ans += 1
    if not ans:
        print(f"Case {rec}: No trees.")
    elif ans == 1:
        print(f"Case {rec}: There is one tree.")
    else:
        print(f"Case {rec}: A forest of {ans} trees.")
    rec += 1