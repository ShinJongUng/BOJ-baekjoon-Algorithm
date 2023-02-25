import sys
input = sys.stdin.readline

t = int(input())

cnt = 0
for i in range(t):
    n, m = input().rstrip().split()
    zero = 0
    one = 0
    for j in range(len(n)):
        if n[j] != m[j]:
            if n[j] == '0':
                zero += 1
            else:
                one += 1
    print(max(zero, one))