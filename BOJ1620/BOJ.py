import sys
input = sys.stdin.readline
N, M = list(map(int, input().rstrip().split()))

dogam = dict()
dogam2 = list()
for i in range(N):
    data = input().rstrip()
    dogam[data] = i + 1
    dogam2.append(data)

for i in range(M):
    data = input().rstrip()
    if data.isdigit():
        print(dogam2[int(data)-1])
    else:
        print(dogam.get(data))
