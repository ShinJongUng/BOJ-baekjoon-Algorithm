import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
ans = 0
for i in range(n):
    cmp = input().rstrip()
    if cmp == s:
        ans += 1
        
print(ans)