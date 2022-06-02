import sys

A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
array=[]
route=[0] * B

for i in range(B):
    x, y=map(int, sys.stdin.readline().split())
    if x>y:
        array.append([x, y+A, i])
    else:
        array.append([x, y, i])
        array.append([x+A, y+A, i])
    
array.sort(key=lambda x:(x[0], -x[1]))
r=0
for i in range(len(array)):
    if r>=array[i][1]:
        route[array[i][2]]=1
    else:
        r=array[i][1]

for i in range(B):
    if not route[i]:
        print(i+1, end=' ')