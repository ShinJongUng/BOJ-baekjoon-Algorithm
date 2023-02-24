import sys
input = sys.stdin.readline

keyboard = {'q': [1, 1, 0], 'w': [1, 2, 0], 'e': [1, 3, 0], 'r': [1, 4, 0], 't': [1, 5, 0],
            'y': [1, 6, 1], 'u': [1, 7, 1], 'i': [1, 8, 1], 'o': [1, 9, 1], 'p': [1, 10, 1],
            'a': [2, 1, 0], 's': [2, 2, 0], 'd': [2, 3, 0], 'f': [2, 4, 0], 'g': [2, 5, 0],
            'h': [2, 6, 1], 'j': [2, 7, 1], 'k': [2, 8, 1], 'l': [2, 9, 1], 'z': [3, 1, 0],
            'x': [3, 2, 0], 'c': [3, 3, 0], 'v': [3, 4, 0], 'b': [3, 5, 1], 'n': [3, 6, 1],
            'm': [3, 7, 1]}

l, r = input().rstrip().split()
arr = list(input().rstrip())
ans = 0
for i in arr:
    iy, ix, hand = keyboard[i]
    if hand:
        ry, rx, rr = keyboard[r]
        rtime = abs(ix - rx) + abs(iy - ry)
        ans += rtime + 1
        r = i
    else:
        ly, lx, ll = keyboard[l]
        ltime = abs(ix - lx) + abs(iy - ly)
        ans += ltime + 1
        l = i
print(ans)