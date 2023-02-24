from collections import deque
N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)

roadNum = [-1] * (N+1) 
roadNum[X] = 0 
queue = deque()
queue.append(X)

while queue :
    now = queue.popleft()
    for next_nod in graph[now] :
        
        if roadNum[next_nod] == -1:
            roadNum[next_nod] = roadNum[now] + 1
            queue.append(next_nod)
check = False

for i in range(1, N+1) :
    if roadNum[i] == K :
        print(i)
        check = True

if check == False :
    print(-1)