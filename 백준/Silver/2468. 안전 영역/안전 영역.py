import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  if rain[x][y] == 1:
    rain[x][y] = 0
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

graph = []
n = int(input())
for i in range(n):
  graph.append(list(map(int, input().split())))

result = 1
cnt = 0
for k in range(1, max(map(max, graph))):
  rain = [[1] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j] <= k:
        rain[i][j] = 0
  for i in range(n):
    for j in range(n):
      if dfs(i, j) == True:
        cnt += 1
  result = max(result, cnt)
  cnt = 0

print(result)