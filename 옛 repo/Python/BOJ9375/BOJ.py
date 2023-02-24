import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    di = dict()
    for _ in range(N):
        a, b = list(map(str, input().split()))
        if b in di:
            nArr = di[b]
            nArr.append(a)
            di[b] = nArr
        else:
            di[b] = [a]
    cnt = 1
    for key in di:
        cnt *= len(di[key]) + 1
    print(cnt - 1)