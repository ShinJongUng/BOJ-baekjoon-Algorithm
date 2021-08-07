N, M = map(int,(input().split()))
a = list(map(int, input().split()))
result = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if a[i]+a[j]+a[k] > M:
                continue
            else:
                result = max(result, a[i] + a[j] + a[k])
print(result)