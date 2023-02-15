import sys
input = sys.stdin.readline

n, k = map(int, input().split())

allballs = 0
for i in range(k + 1):
    allballs += i

if allballs > n:
    print(-1)
else:
    n -= allballs
    if n % k:
        print(k)
    else:
        print(k-1)