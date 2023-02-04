N,K = map(int,input().split())
for i in range(1, N+1):
    if N % i == 0:
        K -= 1
    if K == 0:
        print(i)
        break
else:
    print(0)