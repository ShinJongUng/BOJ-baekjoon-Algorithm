money = int(input())
days = list(map(int, input().split()))
J_money = money
J_cnt = 0
S_money = money
S_cnt = 0

up = 0
down = 0
for i in range(14):
    J_cnt += J_money // days[i]
    J_money %= days[i]
    if i:
        if days[i] > days[i - 1]:
            up += 1
            down = 0
        elif days[i] < days[i - 1]:
            down += 1
            up = 0
        else:
            down = 0
            up = 0
    if down == 3:
        S_cnt += S_money // days[i]
        S_money %= days[i]
    if up == 3:
        S_money += days[i] * S_cnt
        S_cnt = 0


S_money += days[13] * S_cnt
J_money += days[13] * J_cnt

if S_money > J_money:
    print("TIMING")
elif J_money > S_money:
    print("BNP")
else:
    print("SAMESAME")
