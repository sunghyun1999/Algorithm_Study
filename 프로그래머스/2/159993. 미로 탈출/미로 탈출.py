from collections import deque

def bfs(x, y, visited, cnt, step, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y, cnt)])
    visited[x][y] = True
    target_x, target_y = -1, -1
    while queue:
        x, y, cnt = queue.popleft()
        if maps[x][y] == 'L' and step == 0:
            target_x, target_y = x, y
            break
        if maps[x][y] == 'E' and step == 1:
            target_x, target_y = x, y
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny] == False and maps[nx][ny] != "X":
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
    return (target_x, target_y, cnt)

def solution(maps):
    answer = 0
    start_x, start_y = 0, 0
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
    
    lever_x, lever_y, cnt = bfs(start_x, start_y, visited, 0, 0, maps)
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    x, y, answer = bfs(lever_x, lever_y, visited, cnt, 1, maps)
    if x == -1 and y == -1:
        answer = -1
        
    return answer