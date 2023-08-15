from collections import deque
import sys
input = sys.stdin.readline  

m, n, h = map(int, input().split())
graph = []
queue = deque()
for i in range(h):
  arr = []
  for j in range(n):
    tmp = list(map(int, input().split()))
    for k in range(m):
      if tmp[k] == 1:
        queue.append((i, j, k))
    arr.append(tmp)
  graph.append(arr)

dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]  
dz = [-1, 1, 0, 0, 0, 0]

while queue:
  x, y, z = queue.popleft()
  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]
    if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
      continue
    if graph[nx][ny][nz] == -1 or graph[nx][ny][nz] != 0:
      continue
    graph[nx][ny][nz] = graph[x][y][z] + 1
    queue.append((nx, ny, nz))

result = 0
breaker = False
for i in range(h):
  for j in range(n):
    if 0 in graph[i][j]:
      result = -1
      breaker = True
      break
    result = max(result, max(graph[i][j])-1)
  if breaker == True:
    break

print(result)