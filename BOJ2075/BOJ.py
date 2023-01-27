import sys
import heapq
input = sys.stdin.readline
N = int(input())

heap = []
visited = [[0, 0] for _ in range(100002)]
for i in range(N):
    num, hard = list(map(int, input().split()))
    heapq.heappush(heap, (hard, num))
    visited[num][0] = 1
    visited[num][1] = hard

M = int(input())
for i in range(M):
    line = list(map(str, input().strip().split()))
    if line[0] == 'recommend':
        if line[1] == '1':
            cnt = 1
            while cnt <= len(heap):
                s = heapq.nlargest(cnt, heap)[cnt - 1]
                if not visited[s[1]][0]:
                    cnt += 1
                else:
                    if visited[s[1]][1] == s[0]:
                        print(s[1])
                        break
                    else:
                        cnt += 1
        else:
            cnt = 1
            while cnt <= len(heap):
                s = heapq.nsmallest(cnt, heap)[cnt - 1]
                if not visited[s[1]][0]:
                    cnt += 1
                else:
                    if visited[s[1]][1] == s[0]:
                        print(s[1])
                        break
                    else:
                        cnt += 1
    elif line[0] == 'add':
        heapq.heappush(heap, (int(line[2]), int(line[1])))
        visited[int(line[1])][0] = 1
        visited[int(line[1])][1] = int(line[2])
    elif line[0] == 'solved':
        visited[int(line[1])][0] = 0