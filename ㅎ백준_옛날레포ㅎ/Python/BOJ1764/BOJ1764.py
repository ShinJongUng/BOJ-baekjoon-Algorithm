N, M = map(int, input().split())

a = set()
for i in range(N) :
    a.add(input())

b = set()
for i in range(M) :
    b.add(input())

arr = sorted(list(a & b))
print(len(arr))

for i in arr :
    print(i)