import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
check = False
day = 0


def bfs(a, b):
    queue.append((a, b))
    while queue:
      x, y = queue.popleft()
      visited[x][y] = True
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
          if graph[nx][ny] != 0 and not visited[nx][ny]:
            queue.append((nx, ny))
            visited[nx][ny] = True
          elif graph[nx][ny] == 0:
            count[x][y] += 1
    return 1


while True:
  visited = [[False] * m for _ in range(n)]
  count = [[0] * m for _ in range(n)]
  res = []
  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0 and not visited[i][j]:
        res.append(bfs(i, j))

  for i in range(n):
    for j in range(m):
      graph[i][j] -= count[i][j]
      if graph[i][j] < 0:
        graph[i][j] = 0

  if len(res) == 0:
    break
  if len(res) >= 2:
    check = True
    break
  day += 1

if check:
  print(day)
else:
  print(0)
