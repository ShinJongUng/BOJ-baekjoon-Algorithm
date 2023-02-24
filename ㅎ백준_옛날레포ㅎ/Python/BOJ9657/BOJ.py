import sys
input = sys.stdin.readline
arr = list()
N = int(input())
if not N % 7 or N % 7 == 2:
    print("CY")
else:
    print("SK")