import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = 100 - n
b = 100 - m
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
ans = str(n * m)
print(a, b, c, d, q ,r)
print(int(c + q), int(r))