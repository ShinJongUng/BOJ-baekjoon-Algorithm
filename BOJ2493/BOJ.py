import sys
from collections import deque
deq = deque()
list = list()
N = int(input())
line = sys.stdin.readline().rstrip()
ans = 0

for i in range(N):
    list.append(int(input()))

for str in line:
    if(str.isalpha()):
        deq.append(list[ord(str) - 65])
    else:
        first = deq.pop()
        second = deq.pop()
        deq.append(eval(f"{second} {str} {first}"))

print("{:.2f}".format(deq[0]))