import sys
inputs = sys.stdin.readline

N, M = map(int, inputs().split())

board = []

for _ in range(N) :
    board.append(list(map(int, inputs().split())))

for i in range(N) :
    temp = list(map(int, inputs().split()))

    for j in range(M) :
        board[i][j] += temp[j]

for i in range(N) :
    for j in range(M) :
        print(board[i][j], end = " ")
    print()