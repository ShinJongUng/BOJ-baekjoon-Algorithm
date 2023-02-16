import sys
input = sys.stdin.readline

T = int(input())

arr = [1, 1, 2]
for i in range(3, 12):
    arr.append(arr[i-1] + arr[i-2] + arr[i-3])

for _ in range(T):
    n = int(input())
    print(arr[n])