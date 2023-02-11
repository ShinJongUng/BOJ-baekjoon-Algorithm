import sys
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, n * 2 + 1):
        if isPrime(i):
            cnt += 1
    print(cnt)