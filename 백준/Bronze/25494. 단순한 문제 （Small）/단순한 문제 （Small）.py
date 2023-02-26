import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    ans = 0
    for j in range(1, a + 1):
        for k in range(1, b + 1):
            for l in range(1, c + 1):
                if j % k == k % l == l % j:
                    ans += 1
    print(ans)