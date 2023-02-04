import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

print('go' if len(s1) >= len(s2) else 'no')