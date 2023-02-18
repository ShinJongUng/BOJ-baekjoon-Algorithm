import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
line = list(map(int, input().split()))
cnt = 0
for k in range(1, n + 1):
    for i in combinations(line, k):
        if s == sum(i):
            cnt += 1
print(cnt)