from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    

m, n = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
  arr = list(map(int, input().split()))
  for j in range(m):
    if arr[j] == 1:
      queue.append((i, j))
  graph.append(arr)

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if graph[nx][ny] == -1 or graph[nx][ny] != 0:
      continue
    graph[nx][ny] = graph[x][y] + 1
    queue.append((nx, ny))

result = 0
for i in range(n):
  if 0 in graph[i]:
    result = -1
    break
  result = max(result, max(graph[i])-1)

print(result)