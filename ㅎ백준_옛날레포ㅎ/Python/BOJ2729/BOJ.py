N = int(input())

for i in range(N):
    a, b = list((input().split()))
    a = int(a, 2)
    b = int(b, 2)
    print(format(a+b, 'b'))