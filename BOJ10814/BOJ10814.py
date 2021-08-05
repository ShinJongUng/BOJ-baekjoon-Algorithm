N = int(input())

ps = []


for _ in range(N):
    ps.append(list(input().split()))

ps.sort(key=lambda list:int(list[0]))

for i in ps:
    print(i[0], i[1])