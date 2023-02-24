import sys
input = sys.stdin.readline

N, r, c = list(map(int, input().split()))

ans = 0

while N != 0:
    N -= 1
    size = 2 ** N

    # 1사분면
    if r < size and c < size:
        ans += (size ** 2) * 0

    # 2사분면
    elif r < size and c >= size:
        ans += (size ** 2) * 1
        c -= size

    # 3사분면
    elif r >= size and c < size:
        ans += (size ** 2) * 2
        r -= size

    # 4사분면
    else:
        ans += (size ** 2) * 3
        r -= size
        c -= size
print(ans)