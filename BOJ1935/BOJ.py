import sys

input = sys.stdin.readline().rstrip()

list = []
isAns = True
val = 1
ans = 0

for i, str in enumerate(input):
    if str == "(":
        list.append(str)
        val *= 2

    elif str == "[":
        list.append(str)
        val *= 3

    elif str == ")":
        if not list or list[len(list) - 1] == "[":
            isAns = False
            break
        if input[i-1] == "(":
            ans += val
        list.pop()
        val //= 2

    elif str == "]":
        if not list or list[len(list) - 1] == "(":
            isAns = False
            break
        if input[i-1] == "[":
            ans += val
        list.pop()
        val //= 3

if not isAns or list:
    print(0)
else:
    print(ans)