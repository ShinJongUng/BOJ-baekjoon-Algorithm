import sys
input = sys.stdin.readline

paper = [[False] * 100 for _ in range(100)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            paper[j][k] = True


ans = 0
for i in paper:
    ans += i.count(True)

print(ans)