import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs(start, end):
    q = deque()
    q.append((start, ''))
    visited = set()
    visited.add(start)

    while q:
        num, prev = q.popleft()
        if num == end:
            return prev
        if num * 2 >= 10000:#D연산
            if (num * 2) % 10000 not in visited:
                q.append(((num * 2) % 10000, prev + 'D'))
                visited.add((num * 2) % 10000)
        else:
            if num * 2 not in visited:
                q.append((num * 2, prev + 'D'))
                visited.add(num * 2)
        if num == 0:#S연산
            if 9999 not in visited:
                q.append((9999, prev + 'S'))
                visited.add(9999)
        else:
            if num - 1 not in visited:
                q.append((num - 1, prev + 'S'))
                visited.add(num - 1)
        str_num = str(num)
        if len(str_num) != 4:
            str_num = '0' * (4 - len(str_num)) + str_num
        l_command = int(str_num[1:] + str_num[0])
        r_command = int(str_num[len(str_num) - 1] + str_num[:len(str_num) - 1])
        if l_command not in visited:
            q.append((l_command, prev + 'L'))
            visited.add(l_command)
        if r_command not in visited:
            q.append((r_command, prev + 'R'))
            visited.add(r_command)


for _ in range(t):
    a, b = map(int, input().split())
    command = bfs(a, b)
    print(command)
