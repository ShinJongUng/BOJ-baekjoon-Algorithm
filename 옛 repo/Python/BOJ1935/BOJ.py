import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
list = list(map(int, sys.stdin.readline().rstrip().split()))
stack = deque()
ans = [0 for i in range(n)]

for i in range(n):
    while stack:
        if stack[len(stack)-1][1] >= list[i]:
            ans[i] = stack[len(stack)-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, list[i]])

print(" ".join(map(str, ans)))