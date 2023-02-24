import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
no_eat = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    no_eat[a][b] = True
    no_eat[b][a] = True

cnt = 0
for i in combinations(range(1, n+1), 3):
    if no_eat[i[0]][i[1]] or no_eat[i[1]][i[2]] or no_eat[i[0]][i[2]]:
        continue
    cnt += 1

print(cnt)