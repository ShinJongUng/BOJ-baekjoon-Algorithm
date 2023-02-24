import sys
input = sys.stdin.readline
N, X = list(map(int, input().rstrip().split()))
days = list(map(int, input().rstrip().split()))

cnt = 0
max = 0
add = 0
for i in range(N):
    add += days[i]

    if X <= i + 1:
        if i-X >= 0:
            add -= days[i - X]
        if max < add:
            cnt = 1
            max = add
        elif max == add:
            cnt += 1

if max:
    print(max)
    print(cnt)
else:
    print("SAD")