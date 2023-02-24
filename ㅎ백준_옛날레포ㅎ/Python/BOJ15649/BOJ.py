import sys
from itertools import permutations
input = sys.stdin.readline
N, M = list(map(int, input().rstrip().split()))
numbers = [i+1 for i in range(N)]

for i in permutations(numbers, M):
    print(*i)