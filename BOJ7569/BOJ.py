import sys
from collections import deque
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
data = ([deque() for i in range(n+1)])
ans = [0 for i in range(n+1)]

for _ in range(n-1):
    node = list(map(int, sys.stdin.readline().rstrip().split()))
    data[node[0]].append(node[1])
    data[node[1]].append(node[0])

def findAns(idx):
    if(data[idx]):
        node = data[idx].pop()
        if (ans[idx] == node):
            if(data[idx]):
                data[idx].appendleft(node)
                node = idx
            else:
                node = ans[idx]
        else:
            ans[node] = idx
        findAns(node)

findAns(1)

print("\n".join(map(str, ans[2:])))