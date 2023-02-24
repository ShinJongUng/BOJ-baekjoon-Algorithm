import sys
input = sys.stdin.readline

arr = [1, 1, 1]

for i in range(3, 101):
    arr.append(arr[i-3] + arr[i-2])

t = int(input())

for i in range(t):
    n = int(input())
    print(arr[n - 1])
