import sys
input = sys.stdin.readline
N, M = list(map(int, input().rstrip().split()))

A = list(map(int, input().rstrip().split()))
A.extend(list(map(int, input().rstrip().split())))

print(*sorted(A))

