import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
arr = sorted(list(map(int, input().split())))
for i in combinations(arr, m):
    print(" ".join(map(str, i)))