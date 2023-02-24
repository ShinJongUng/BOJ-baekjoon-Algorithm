import math
import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))

ans = dict()
for i in range(n):
    site, password = list(input().rstrip().split())
    ans[site] = password

for i in range(m):
    site = input().rstrip()
    print(ans[site])