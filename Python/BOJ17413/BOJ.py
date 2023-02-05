import sys
input = sys.stdin.readline

s = input().rstrip()

stack = []
isTag = False
for i in s:
    if i != ' ' or isTag:
        if i == '<':
            print(''.join(map(str, reversed(stack))), end='')
            stack.clear()
            isTag = True
        if i == '>':
            print(''.join(map(str, stack)), end='>')
            stack.clear()
            isTag = False
            continue
        stack.append(i)
    else:
        print(''.join(map(str, reversed(stack))), end=' ')
        stack.clear()

print(''.join(map(str, reversed(stack))), end='')