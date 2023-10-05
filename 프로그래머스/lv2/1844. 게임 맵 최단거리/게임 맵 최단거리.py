from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        x, y, cnt = queue.popleft()
        if x == n-1 and y == m-1:
            answer = cnt
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    
    return answer