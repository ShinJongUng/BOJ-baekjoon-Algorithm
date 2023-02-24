import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []
for i in range(p):
    l, n = map(str, input().split())
    l = int(l)
    if not room:
        room.append([[n, l]])
    else:
        flag = False
        for i in range(len(room)):
            if abs(room[i][0][1] - l) <= 10 and len(room[i]) < m:
                room[i].append([n, l])
                flag = True
                break
        if not flag:
            room.append([[n, l]])

for r in room:
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    for n, l in sorted(r):
        print(l, n)