from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visit = [[False] * m for _ in range(n)]
queue = deque()

for i in range(n):
  arr = list(map(int, input().split()))
  for j in range(m):
    if arr[j] == 2:
      arr[j] = 0
      queue.append((i, j))
      visit[i][j] = True
  graph.append(arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >=n or ny < 0 or ny >=m:
      continue
    if visit[nx][ny] == True:
      continue
    if visit[nx][ny] == False:
      if graph[nx][ny] == 0:
        continue
      else:
        visit[nx][ny] = True
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

for i in range(n):
  for j in range(m):
    if visit[i][j] == False and graph[i][j] != 0:
      graph[i][j] = -1

for i in range(n):
  for j in range(m):
    print(graph[i][j], end=' ')
  print()