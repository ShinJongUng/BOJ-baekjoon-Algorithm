import sys
input = sys.stdin.readline
words_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
while True:
	n = input().rstrip()
	cnt = 0
	if n == '#':
		break
	for i in n:
		if i in words_set:
			cnt += 1
	print(cnt)
   