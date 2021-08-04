T=int(input())

for i in range(T):
    N, M =map(int,input().split())
        
    value=1
    
    if N!=0:
        for j in range(N): value*=(M-j)
        for j in range(1,N+1): value=value//j

    print(value)
