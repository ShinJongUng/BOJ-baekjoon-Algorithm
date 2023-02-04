import sys
input = sys.stdin.readline

line = input().rstrip()

stack = []
isLaser = False
ans = 0
for idx in line:
    if idx == '(':
        stack.append(0)
        isLaser = True
    elif idx == ')':
        if isLaser:
            stack.pop()
            for i in range(len(stack)):
                stack[i] += 1
            isLaser = False
        else:
            l_cnt = stack.pop()
            ans += l_cnt + 1
print(ans)