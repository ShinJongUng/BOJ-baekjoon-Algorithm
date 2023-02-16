import sys
input = sys.stdin.readline

line = input().rstrip().split('-')

numbers = []
for i in range(len(line)):
    sums = 0
    s = line[i].split('+')
    for j in s:
        sums += int(j)
    numbers.append(sums)
ans = numbers[0]

for i in range(1, len(numbers)):
    ans -= numbers[i]
print(ans)