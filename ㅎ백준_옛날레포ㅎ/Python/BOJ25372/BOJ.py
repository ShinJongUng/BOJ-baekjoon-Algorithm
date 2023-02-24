import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    line = input().rstrip()
    print("yes" if 6 <= len(line) <= 9 else "no")