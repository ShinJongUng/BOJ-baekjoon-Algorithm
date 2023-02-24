import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
rope = list(int(input().rstrip()) for _ in range(N))
rope = deque(sorted(rope))
ans = rope[0]

for i in range(N):
    item = rope.popleft()
    ans = max(ans, item * (len(rope) + 1))

print(ans)