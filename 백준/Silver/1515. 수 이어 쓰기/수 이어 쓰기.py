import sys
from collections import deque
input = sys.stdin.readline

line = deque(input().rstrip())
num = 1
while line:
    num_str = str(num)

    for i in num_str:
        if line and line[0] == i:
            line.popleft()
    if not line:
        break
    num += 1
print(num)