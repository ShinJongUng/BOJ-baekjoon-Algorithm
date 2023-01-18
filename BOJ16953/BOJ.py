import sys
from collections import deque
input = sys.stdin.readline
A, B = list(map(int, input().rstrip().split()))


q = deque()
q.append([A, 0])

while q:
    n = q.popleft()

    if n[0] == B:
        print(n[1] + 1)
        exit(0)
    for i in [n[0] * 2, int(str(n[0]) + '1')]:
        if i > B:
            continue
        q.append([i, n[1] + 1])

print(-1)