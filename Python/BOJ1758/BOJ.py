import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for i in range(n):
    num = arr[i] - ((i+1) - 1)
    if num > 0:
        ans += num
print(ans)