import sys
input = sys.stdin.readline

def dfs(v, i):
  visited[v] = True
  val = arr[v]
  if not visited[val]:
    dfs(val, i)
  elif visited[val] and val == i:
    result.append(val)

n = int(input())
arr = [0]
for _ in range(n):
  arr.append(int(input()))

result = []
visited = [False] * (n+1)
for i in range(1, n+1):
  dfs(i, i)
  visited = [False] * (n+1)

print(len(result))
for num in sorted(result):
  print(num)