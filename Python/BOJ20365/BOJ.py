import sys
input = sys.stdin.readline
n = int(input())
arr = list(input().strip())


cnt1 = 1
flag = False
x = 'R'
for i in arr:
    if x != i:
        if not flag:
            flag = True
            cnt1 += 1
    else:
        flag = False

cnt2 = 1
flag = False
x = 'B'
for i in arr:
    if x != i:
        if not flag:
            flag = True
            cnt2 += 1
    else:
        flag = False


print(min(cnt1, cnt2))