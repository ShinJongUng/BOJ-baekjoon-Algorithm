import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #사람 수, 파티 수
know_people = list(map(int, input().split()))
parent = [i for i in range(n + 1)]

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    if a != b:
        a = find(a)
        b = find(b)

        if a < b:
            parent[a] = b
        else:
            parent[b] = a

temp = []
ans = 0
for i in range(m):
    line = list(map(int, input().split()))
    temp.append(line[1:])
    for j in range(1, line[0] + 1):
        union(line[1], line[j])

for i in range(n):
    find(i)

check = set()
if len(know_people) >= 2:
    for i in know_people[1:]:
        check.add(find(i))
else:
    print(m)
    exit(0)

for i in range(m):
    flag = False
    for j in temp[i]:
        if parent[j] in check:
            flag = True
            break
    if not flag:
        ans += 1

print(ans)