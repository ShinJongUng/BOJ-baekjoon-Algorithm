import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
n, m = map(int, input().split())
line = sorted(list(map(int, input().split())))
visit = set()

for i in combinations_with_replacement(line, m):
    if i not in visit:
        visit.add(i)
        print(*i)