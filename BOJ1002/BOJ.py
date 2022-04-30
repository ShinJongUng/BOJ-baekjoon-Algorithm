test = int(input())

for _ in range(test):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
        print(0)
    elif r1 == distance + r2 or r2 == distance + r1 or r1 + r2 == distance:
        print(1)
    else:
        print(2)