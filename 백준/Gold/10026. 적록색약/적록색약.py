import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  if visited[x][y] == True:
    return False
  if visited[x][y] == False:
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        if visited[nx][ny] == False and graph[x][y] == graph[nx][ny]:
          dfs(nx, ny)
    return True
  return False

graph = []
n = int(input())
cnt1, cnt2 = 0, 0
visited = [[False] * n for _ in range(n)]
for _ in range(n):
  graph.append(list(input()))

for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      cnt1 += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'

for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      cnt2 += 1
    
print(cnt1, cnt2)