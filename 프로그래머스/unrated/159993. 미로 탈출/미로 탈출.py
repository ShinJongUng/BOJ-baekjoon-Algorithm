from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(x1, y1, x2, y2, maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append([y1, x1])
    visited[y1][x1] = 1
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if not visited[ny][nx] and maps[ny][nx] != 'X':
                q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                if ny == y2 and nx == x2:
                    return visited[ny][nx] - 1
    return -1

def solution(maps):
    s_idx, l_idx, e_idx = [0, 0], [0, 0], [0, 0] #x, y
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if 'L' == maps[i][j]:
                l_idx = [j, i]
            if 'S' == maps[i][j]:
                s_idx = [j, i]
            if 'E' == maps[i][j]:
                e_idx = [j, i]
    
    s_to_l = BFS(s_idx[0], s_idx[1], l_idx[0], l_idx[1], maps)
    l_to_e = BFS(l_idx[0], l_idx[1], e_idx[0], e_idx[1], maps)
    if s_to_l == -1 or l_to_e == -1:
        return -1
    else:
        return s_to_l + l_to_e
    
        