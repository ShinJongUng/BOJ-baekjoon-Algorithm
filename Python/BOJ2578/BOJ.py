bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

callNum = []
for _ in range(5):
    callNum.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        number = callNum[i][j]
        for k in range(5):
            if number in bingo[k]:
                s = bingo[k].index(number)
                bingo[k][s] = 0
                break
        cnt = 0
        col = [0] * 5
        dia = [0] * 2
        for k in range(5):
            isBingo = True
            for s in range(5):
                if not bingo[k][s]:
                    if not isBingo:
                        isBingo = False
                    if k == s:
                        dia[0] += 1
                    if k + s == 4:
                        dia[1] += 1
                    col[s] += 1
                else:
                    isBingo = False
            if isBingo:
                cnt += 1
        if 5 in col:
            for k in range(5):
                if col[k] >= 5:
                    cnt += 1
        if 5 in dia:
            for k in range(2):
                if dia[k] >= 5:
                    cnt += 1
        if cnt >= 3:
            print(i * 5 + j + 1)
            exit(0)