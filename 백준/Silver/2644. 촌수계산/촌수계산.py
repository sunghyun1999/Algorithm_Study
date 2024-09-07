n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(v, num):
  global is_relative
  visited[v] = True
  if v == b:
    is_relative = True
    print(num)
    return

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num+1)

is_relative = False
dfs(a, 0)
if is_relative is False:
  print(-1)
  