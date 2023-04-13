from collections import deque

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  cnt = 1

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        cnt += 1
        queue.append((nx, ny))

  result.append(cnt)

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      graph[i][j] = 0
      bfs(i, j)

print(len(result))
for i in sorted(result):
  print(i)