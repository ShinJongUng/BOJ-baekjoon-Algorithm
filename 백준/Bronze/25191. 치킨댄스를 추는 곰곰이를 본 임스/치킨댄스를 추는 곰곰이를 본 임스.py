import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

ans = 0
for i in range(n):
    if a >= 2:
        a -= 2
        ans += 1
    elif b != 0:
        b -= 1
        ans += 1
print(ans)