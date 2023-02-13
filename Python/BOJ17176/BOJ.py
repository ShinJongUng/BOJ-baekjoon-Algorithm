import sys
from collections import deque
input = sys.stdin.readline
# 아스키 A: 65, Z:90, a:97, z:122

n = int(input())
words_number = list(map(int, input().split()))
words_dict = dict()

for i in words_number:
    if i in words_dict:
        words_dict[i] += 1
    else:
        words_dict[i] = 1

words = list(input())

for i in words:
    if i == ' ':
        if 0 in words_dict:
            words_dict[0] -= 1
        else:
            print('n')
            exit(0)
    elif 'A' <= i <= 'Z':
        if ord(i) - 64 in words_dict and words_dict[ord(i) - 64] > 0:
            words_dict[ord(i) - 64] -= 1
        else:
            print('n')
            exit(0)
    elif 'a' <= i <= 'z':
        if ord(i) - 70 in words_dict and words_dict[ord(i) - 70] > 0:
            words_dict[ord(i) - 70] -= 1
        else:
            print('n')
            exit(0)
print("y")