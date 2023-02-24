import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
line = sorted(list(map(int, input().split())))
visit = set()

for i in permutations(line, m):
    if i not in visit:
        visit.add(i)
        print(*i)