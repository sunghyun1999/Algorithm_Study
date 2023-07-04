import sys
input = sys.stdin.readline

def dfs(v):
  visited[v] = 1
  for nv in graph[v]:
    if visited[nv] == 0:
      dfs(nv)

n = int(input())
connect = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(connect):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
print(sum(visited)-1)