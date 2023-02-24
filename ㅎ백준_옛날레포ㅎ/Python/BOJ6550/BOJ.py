import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        cnt = 0
        for i in range(len(t)):
            if t[i] == s[cnt]:
                cnt += 1
                if cnt == len(s):
                    break
        if cnt == len(s):
            print("Yes")
        else:
            print("No")

    except:
        break