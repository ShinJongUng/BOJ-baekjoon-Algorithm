import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list()
title = list()

for i in range(n):
    a, b = map(str, input().split())
    if nums and int(b) == nums[-1]:
        continue
    nums.append(int(b))
    title.append(a)


def bs(num):
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if num > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return title[right + 1]

for _ in range(m):
    s = int(input())
    print(bs(s))
