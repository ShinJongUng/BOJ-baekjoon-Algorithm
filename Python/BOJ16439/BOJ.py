import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

numbers = []
maxnum = 0
for i in combinations(range(m), 3):
    likes = 0
    for j in range(n):
        likes += max(arr[j][i[0]], arr[j][i[1]], arr[j][i[2]])
    maxnum = max(maxnum, likes)

print(maxnum)