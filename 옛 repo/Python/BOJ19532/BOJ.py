from itertools import combinations
line = list(map(int, input().split()))


for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (line[0] * j) + (line[1] * i) == line[2] and (line[3] * j) + (line[4] * i) == line[5]:
            print(j, i)
            exit(0)