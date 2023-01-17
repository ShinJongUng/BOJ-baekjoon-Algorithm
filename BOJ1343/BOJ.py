import sys
input = sys.stdin.readline

line = list(input().rstrip())

cnt = 0
isAns = True
for i in range(len(line)):
    if line[i] == 'X':
        cnt += 1
        if cnt == 4:
            line[i] = line[i - 1] = line[i - 2] = line[i - 3] = 'A'
            cnt -= 4
    elif line[i] == '.':
        if cnt == 2:
            line[i - 1] = line[i - 2] = 'B'
            cnt -= 2
        else:
            if cnt:
                isAns = False
if cnt >= 2:
    line[-1] = line[-2] = 'B'
    cnt = 0

if 'X' in line or not isAns or cnt > 0:
    print(-1)
else:
    print("".join(map(str, line)))