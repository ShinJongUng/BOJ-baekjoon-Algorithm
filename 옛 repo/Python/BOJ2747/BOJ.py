import sys
input = sys.stdin.readline
arr = [0, 1]
N = int(input())
for i in range(2, N+1):
    arr.append(arr[i - 2] + arr[i - 1])

print(arr[N])