import sys
input = sys.stdin.readline
line = list(input().rstrip())
op = {"+": 1, "-": 1, "*":2, "/":2, "(":3, ")":3}
arr = []
for i in line:
    if i.isalpha():
        print(i, end="")
    else:
        if not arr:
            arr.append(i)
        else:
            depth = 0
            flag = False
            while arr:
                if i == '(':
                    depth += 1
                if i == ')':
                    flag = True
                    depth -= 1
                if flag:
                    n = arr.pop()
                    if n == '(':
                        flag = False
                        break
                    else:
                        print(n, end="")
                else:
                    if op[arr[-1]] >= op[i] and arr[-1] != '(':
                        data = arr.pop()
                        print(data, end="")
                        if not arr:
                            arr.append(i)
                            break
                    else:
                        arr.append(i)
                        break
while arr:
    print(arr.pop(), end="")

