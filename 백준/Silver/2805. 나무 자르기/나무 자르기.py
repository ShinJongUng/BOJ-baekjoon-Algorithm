import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
left, right = 0, max(arr)
while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            temp += arr[i] - mid

    if temp >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)