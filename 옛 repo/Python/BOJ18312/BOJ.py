N, K = list(map(int, input().split()))
cnt = 0
for i in range(0, N+1):
    for j in range(60):
        for k in range(60):
            if len(str(i)) == 1:
                i = '0' + str(i)
            if len(str(j)) == 1:
                j = '0' + str(j)
            if len(str(k)) == 1:
                k = '0' + str(k)
            time = str(i) + str(j) + str(k)
            if str(K) in time:
                cnt += 1
print(cnt)