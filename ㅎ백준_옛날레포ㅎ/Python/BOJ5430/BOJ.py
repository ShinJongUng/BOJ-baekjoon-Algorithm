import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    isError = False
    rcnt = 0
    for x in p:
        if x == 'R':
            rcnt += 1
        elif x == 'D':
            if n == 0:
                isError = True
                break
            if arr:
                if rcnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                isError = True
                break
    if rcnt % 2 == 1:
        arr.reverse()

    print("["+",".join(map(str, arr))+"]" if not isError else "error")

