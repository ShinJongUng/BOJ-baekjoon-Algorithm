import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()

for i in range(n):
    s = input().rstrip()
    if s not in words:
        words[s] = 1
    else:
        words[s] += 1

arr = []
for i in words.keys():
    if len(i) >= m:
        arr.append((words[i], i))
arr.sort(key=lambda x: (-x[0], -1 * len(x[1]), x[1]))

for i in arr:
    print(i[1])