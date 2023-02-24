import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
r_buttons = []
if M:
    r_buttons = list(map(str, input().split()))
buttons = [i for i in range(10) if str(i) not in r_buttons]

cmp_min = 100
for i in range(1000001):
    flag = True
    for j in r_buttons:
        if str(j) in str(i):
            flag = False
            break
    if flag:
        if abs(N - cmp_min) > abs(N - i):
            cmp_min = i

if abs(N - cmp_min) + len(str(cmp_min)) >= abs(100 - N):
    print(abs(100 - N))
else:
    print(abs(N - cmp_min) + len(str(cmp_min)))