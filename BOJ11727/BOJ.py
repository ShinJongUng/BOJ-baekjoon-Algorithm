import sys
input = sys.stdin.readline

n = int(input())
ans = [1, 1]

if n >= 2:
    for i in range(2, n + 1):
        ans.append(ans[i - 1] + ans[i - 2])
    print(ans[n] % 10007)
else:
    print(1)