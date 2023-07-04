import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
  for nv in graph[v]:
    if parent[nv] == 0:
      parent[nv] = v
      dfs(nv)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
for i in range(2, n+1):
  print(parent[i])