import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
drinks = deque(sorted(list(map(int, input().split())), reverse=True))

while len(drinks) != 1:
    large = drinks.popleft()
    small = drinks.pop()
    drinks.appendleft(large + (small / 2))

print(int(drinks[0]) if drinks[0] % 1 == 0 else drinks[0])