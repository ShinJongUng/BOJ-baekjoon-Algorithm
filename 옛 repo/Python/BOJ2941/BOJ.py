a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
inputs = input()
cnt = 0
for i in a:
    inputs = inputs.replace(i, 'a')

for _ in inputs:
    cnt += 1
    
print(cnt)