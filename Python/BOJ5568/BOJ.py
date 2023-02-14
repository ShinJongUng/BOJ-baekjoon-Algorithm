import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())
numbers = [int(input()) for _ in range(n)]
cards = dict()

for i in permutations(numbers, k):
    card = "".join(map(str, i))
    if card not in cards:
        cards[card] = 1

print(len(cards))
