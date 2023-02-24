import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
line = sorted(list(map(int, input().split())))
for i in permutations(line, m):
    print(*i)