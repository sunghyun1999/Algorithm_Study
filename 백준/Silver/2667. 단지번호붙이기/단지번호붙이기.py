import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
  global cnt
  if x < 0 or x >= n or y < 0 or y >= n:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 2
    cnt += 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

graph = []
n = int(input())
for i in range(n):
  graph.append(list(map(int, input())))

result = []
cnt = 0
for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      result.append(cnt)
      cnt = 0

print(len(result))
for i in sorted(result):
  print(i)