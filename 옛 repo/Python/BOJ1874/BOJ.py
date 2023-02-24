N = int(input())
count = 1
isTrue = True
stack = []
arr = []
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        arr.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        isTrue = False
        break
if isTrue == False:
    print("NO")
else:
    for i in arr:
        print(i)