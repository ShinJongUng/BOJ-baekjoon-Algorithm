import sys
input = sys.stdin.readline

n, k = map(int, input().split())

x = sorted(list(map(int, input().split())), reverse=True)

print(x[k-1])