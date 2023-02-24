N = int(input())
arr = [i+1 for i in range(N)]
cnt = 0
if N == 1: print(1); exit(0)
while(True):
    nCnt = 0
    for i in range(N):
        if i % 2 == 0 or not arr[i]:
            arr[i] = 0
        else:
            nCnt += 1
            arr[i - nCnt] = arr[i]
            arr[i] = 0
    cnt += 1
    if nCnt == 1:
        print(arr[0])
        break