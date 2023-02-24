import sys
input = sys.stdin.readline
n = int(input())
roads = list(map(int, input().split()))
city = list(map(int, input().split()))

ans = 0
minimum = sys.maxsize
for i in range(len(roads)):
    road = roads[i]
    minimum = min(minimum, city[i])
    ans += road * minimum

print(ans)