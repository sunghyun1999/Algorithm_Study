from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
  visited = [0] * (n+1)
  visited[v] = 1
  queue = deque([v])
  cnt = 1
  while queue:
    c = queue.popleft()
    for nv in graph[c]:
      if visited[nv] == 0:
        queue.append(nv)
        visited[nv] = 1
        cnt += 1
  result[v] = cnt
 
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

for i in range(1, n+1):
  bfs(i)

for i in range(1, n+1):
  if result[i] == max(result):
    print(i, end=' ')