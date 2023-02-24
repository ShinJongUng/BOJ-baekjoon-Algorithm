from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while queue:
        b = max(queue)  
        f = queue.popleft() 
        m -= 1

        if b == f: # 
            cnt += 1 
            if m < 0: 
                print(cnt)
                break

        else:  
            queue.append(f) 
            if m < 0 :  
                m = len(queue) - 1 