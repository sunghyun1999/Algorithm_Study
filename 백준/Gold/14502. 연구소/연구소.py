from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
temp = [[0] * m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def bfs():
  global result
  queue = deque()

  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if temp[nx][ny] == 0:
          temp[nx][ny] = 2
          queue.append((nx, ny))

  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  result = max(result, score)

def wall(cnt):
  if cnt == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        cnt += 1
        wall(cnt)
        graph[i][j] = 0
        cnt -= 1

wall(0)
print(result)