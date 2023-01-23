import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

ans = 0
sum = 0
for minute in arr:
    ans += minute + sum
    sum += minute

print(ans)