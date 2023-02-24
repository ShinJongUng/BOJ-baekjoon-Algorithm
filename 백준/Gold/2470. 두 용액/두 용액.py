import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = []
min_num = sys.maxsize
left, right = 0, len(arr) - 1
while left < right:
    if abs(arr[left] + arr[right]) < min_num:
        min_num = abs(arr[left] + arr[right])
        ans = [arr[left], arr[right]]
    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -= 1

print(*ans)