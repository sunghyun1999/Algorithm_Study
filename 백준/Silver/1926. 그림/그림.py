from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 1

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if paper[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
