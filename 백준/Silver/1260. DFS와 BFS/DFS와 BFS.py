from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
  visited[v] = 1
  print(v, end=' ')
  for nv in graph[v]:
    if visited[nv] == 0:
      dfs(nv)

def bfs(v):
  visited[v] = 1
  print(v, end=' ')
  queue = deque([v])
  while queue:
    c = queue.popleft()
    for nv in graph[c]:
      if visited[nv] == 0:
        queue.append(nv)
        visited[nv] = 1
        print(nv, end=' ')

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1):
  graph[i].sort()

dfs(v)
visited = [0] * (n+1)
print()
bfs(v)