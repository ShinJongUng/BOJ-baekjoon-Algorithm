import heapq
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n, k, t_id, m = map(int, input().split())
    score = {i: dict() for i in range(n + 1)}
    cnt = [0] * (n + 1)
    time = [0] * (n + 1)
    for j in range(m):
        tt_id, number, sco = map(int, input().split())
        if not score[tt_id].get(number):
            score[tt_id][number] = sco
        else:
            score[tt_id][number] = max(score[tt_id][number], sco)
        cnt[tt_id] += 1
        time[tt_id] = j
    ans = [[0, 0, 0, 0] for _ in range(n + 1)] #점수, 제출 횟수, 마지막 제출 시간
    ans[0] = [-1, -1, -1, -1]
    for i in range(1, n + 1):
        ans[i][1] = -cnt[i]
        ans[i][2] = -time[i]
        ans[i][3] = i
        for j in score[i].values():
            ans[i][0] += j

    arr = heapq.nlargest(n + 1, ans)
    for i in range(n):
        if arr[i][3] == t_id:
            print(i + 1)
            break
