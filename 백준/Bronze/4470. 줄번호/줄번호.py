import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
	n = input().rstrip()
	print(f"{i+1}.", n)