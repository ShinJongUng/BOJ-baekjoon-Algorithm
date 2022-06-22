n = int(input())
lists = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in lists:
    if(i == v):
        cnt += 1

print(cnt)