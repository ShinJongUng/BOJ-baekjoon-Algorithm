import sys
input = sys.stdin.readline

x = int(input())
n = int(input())

ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += a * b

print("Yes" if ans == x else "No")