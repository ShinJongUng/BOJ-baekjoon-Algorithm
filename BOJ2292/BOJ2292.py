N = int(input())
start = 1
plus = 6
room = 1

while start < N :
        start = start + plus
        room+= 1
        if N <= start:
            print(room)
            break
        plus += 6

else:
    print(1)