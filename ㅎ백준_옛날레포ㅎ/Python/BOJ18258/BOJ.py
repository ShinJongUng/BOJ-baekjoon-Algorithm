import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    line = list(input().rstrip().split())
    if line[0] == 'push':
        q.append(line[1])
    elif line[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(q))
    elif line[0] == 'empty':
        print(0 if q else 1)
    elif line[0] == 'front':
        print(q[0] if q else -1)
    elif line[0] == 'back':
        print(q[-1] if q else -1)
