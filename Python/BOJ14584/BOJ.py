import sys
input = sys.stdin.readline
#122
line = input().rstrip()
n = int(input())
data = []
for i in range(n):
    data.append(input().rstrip())

for i in range(1, 27):
    n_line = ''
    for j in range(len(line)):
        s = ord(line[j]) + i
        if s > 122:
            s -= 26
        n_line += chr(s)
    flag = False
    for j in data:
        if n_line.count(j):
            flag = True
            break
    if flag:
        print(n_line)
        break
