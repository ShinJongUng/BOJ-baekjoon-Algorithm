import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
  start, end = map(int, input().split())
  arr.append([start, end])

arr = sorted(arr, key=lambda a: a[0])
arr = sorted(arr, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in arr:
  if i >= last:
    cnt += 1
    last = j

print(cnt)