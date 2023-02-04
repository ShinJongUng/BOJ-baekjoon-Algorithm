# 100점
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
cnt = 0
ans = 0
index = 0

while index < m - 1:
    if s[index:index+3] == 'IOI':
        index += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        index += 1
        cnt = 0
print(ans)

#50점
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
cnt = 0
cmpstr = 'IO' * n + 'I'
q = deque(maxlen=n * 2 + 1)
for i in range(m):
    q.append(s[i])
    if cmpstr == ''.join(q):
        cnt += 1

print(cnt)