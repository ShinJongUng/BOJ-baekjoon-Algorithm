import sys
input = sys.stdin.readline

n = int(input())
ans = [0, 1]

if n >= 2:
    for i in range(2, n + 1):
        if i % 2 == 0:
            ans.append(ans[i - 1] * 2 + 1)
        else:
            ans.append(ans[i - 1] * 2 - 1)
    print(ans[n] % 10007)
else:
    print(1)