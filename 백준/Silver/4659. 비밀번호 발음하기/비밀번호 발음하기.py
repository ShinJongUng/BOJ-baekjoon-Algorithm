import sys
input = sys.stdin.readline
words = set(['a', 'e', 'i', 'o', 'u'])

while True:
    line = input().rstrip()
    if line == 'end':
        break
    flag1 = False
    flag2 = True
    count2 = []
    flag3 = True
    prev_word = ''
    for i in line:
        if i in words:
            flag1 = True
            count2.append(1)
        else:
            count2.append(0)
        if len(count2) > 3:
            count2.pop(0)
        if count2.count(0) == 3 or count2.count(1) == 3:
            flag2 = False
            break
        if i == prev_word:
            if i != 'e' and i != 'o':
                flag3 = False
        prev_word = i

    if flag1 and flag2 and flag3:
        print(f"<{line}> is acceptable.")
    else:
        print(f"<{line}> is not acceptable.")