import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(3):
    if arr[i] <= n:
        ans += arr[i]
    else:
        ans += n
print(ans)