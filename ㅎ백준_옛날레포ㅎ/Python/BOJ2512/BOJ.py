import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

if sum(arr) <= m:
    print(max(arr))
else:
    left = 0
    right = max(arr)
    while left <= right:
        mid = (left + right) // 2

        total = 0
        for i in arr:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= m:
            left = mid + 1
        else:
            right = mid - 1
    print(right)