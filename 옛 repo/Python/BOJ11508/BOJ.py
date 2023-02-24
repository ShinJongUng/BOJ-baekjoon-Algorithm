import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for i in range(2, n, 3):
    ans += arr[i]

print(sum(arr) - ans)