import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(input().rstrip()) for _ in range(n)]

length = len(numbers[0])

for i in range(length - 1, -1, -1):
    name_set = set()
    flag = False
    for j in range(len(numbers)):
        number = "".join(numbers[j][i:])
        if number in name_set:
            flag = True
            break
        else:
            name_set.add(number)
    if not flag:
        print(length - i)
        break