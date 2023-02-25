import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in product(arr, repeat=m):
    print(*i)