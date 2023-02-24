import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())

def recursive(n):
    if n <= 1:
        return 1
    else:
        return n * recursive(n-1)

num = str(recursive(N))
cnt = 0
for i in range(len(num)-1, 0, -1):
    if num[i] == '0':
        cnt += 1
    else:
        break

print(cnt)