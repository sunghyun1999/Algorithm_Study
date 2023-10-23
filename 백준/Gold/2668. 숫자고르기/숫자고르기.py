n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
  num = int(input())
  graph[num].append(i)

visited = [False] * (n+1)

result = []
def dfs(v, route):
  route.add(v)
  visited[v] = True
  for i in graph[v]:
    if i not in route:
      dfs(i, route.copy())
    else:
      result.extend(list(route))
      return

for i in range(1, n+1):
  if not visited[i]:
    dfs(i, set([]))

result.sort()
print(len(result))
for num in result:
  print(num)