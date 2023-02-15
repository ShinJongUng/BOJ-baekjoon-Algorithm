import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.extend(reversed(arr))

for i in range(len(arr)):
    k -= arr[i]
    if k < 0:
        print(i + 1 if i <= n - 1 else n - i + n)
        break