import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
for i in range(len(arr) - 2):
    if arr[i] < arr[i+1] + arr[i+2]:
        print(arr[i] + arr[i+1] + arr[i+2])
        exit(0)

print(-1)