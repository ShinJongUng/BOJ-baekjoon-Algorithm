import heapq
import sys
input = sys.stdin.readline

s = int(input())
switchs = list(map(int, input().split()))

n = int(input())

def change_switch(num):
    if switchs[num]:
        switchs[num] = 0
    else:
        switchs[num] = 1

for i in range(n):
    sex, num = map(int, input().split())
    if sex == 1:
        multi = num
        while multi <= s:
            change_switch(multi - 1)
            multi += num
    elif sex == 2:
        change_switch(num - 1)
        upper = num + 1
        lower = num - 1
        while True:
            if upper > s or lower <= 0:
                break
            if switchs[upper - 1] != switchs[lower - 1]:
                break
            change_switch(upper - 1)
            change_switch(lower - 1)
            upper += 1
            lower -= 1

for i in range(1, s + 1):
    print(switchs[i - 1], end=" ")
    if i % 20 == 0:
        print()

