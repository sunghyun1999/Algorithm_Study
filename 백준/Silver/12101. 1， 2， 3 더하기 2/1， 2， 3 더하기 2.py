import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

res = []
def dfs(arr, n):
  if sum(arr) == n:
    res.append(arr.copy())
    return
  if sum(arr) < n:
    for num in [1, 2, 3]:
      arr.append(num)
      dfs(arr, n)
      arr.pop()

dfs([], n)
res.sort()
if len(res) < k:
  print(-1)
else:
  print('+'.join(map(str, res[k-1])))