import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minimum = sys.maxsize
for i in range(1, n + 1):
    for j in combinations(arr, i):
        sin = j[0][0]
        ssen = j[0][1]
        for k in range(1, len(j)):
            sin *= j[k][0]
            ssen += j[k][1]
        minimum = min(minimum, abs(sin - ssen))

print(minimum)