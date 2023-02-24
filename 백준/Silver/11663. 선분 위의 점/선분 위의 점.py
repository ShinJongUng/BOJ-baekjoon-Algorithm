import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dot_arr = sorted(list(map(int, input().split())))

for i in range(m):
    a, b = map(int, input().split())
    left, right = 0, len(dot_arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if dot_arr[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    start = right
    left, right = 0, len(dot_arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if dot_arr[mid] <= b:
            left = mid + 1
        else:
            right = mid - 1

    print(right - start)