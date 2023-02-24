import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mem = [[0] * (i+1) for i in range(n)]
mem[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j != 0:
            mem[i][j] = max(mem[i][j], mem[i - 1][j - 1] + arr[i][j])
        if j != i:
            mem[i][j] = max(mem[i][j], mem[i - 1][j] + arr[i][j])

print(max(mem[n - 1]))