import sys
from itertools import combinations
input = sys.stdin.readline
N, M = list(map(int, input().rstrip().split()))
numbers = [i+1 for i in range(N)]

for i in combinations(numbers, M):
    print(*i)