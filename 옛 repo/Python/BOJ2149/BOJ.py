import sys
input = sys.stdin.readline

n_key = input().rstrip()
n_value = input().rstrip()

line = ['' for _ in range(len(n_key))]

idx = 0
for i in range(len(n_value)):
    line[idx] += n_value[i]
    if len(line[idx]) >= len(n_value) // len(n_key):
        idx += 1

n_dict = dict()
s_key = sorted(n_key)
for i in range(len(n_key)):
    if s_key[i] not in n_dict:
        n_dict[s_key[i]] = [i]
    else:
        n_dict[s_key[i]].append(i)

key_list = []
for i in n_key:
    key_list.append(n_dict[i].pop(0))

for i in range(len(n_value) // len(n_key)):
    for j in key_list:
        print(line[j][i], end='')
