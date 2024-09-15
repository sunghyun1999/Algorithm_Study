from collections import deque

def bfs(a, b):
  queue = deque()
  queue.append(a)
  while queue:
    x = queue.popleft()
    if x == b:
      print(dist[x])
      break
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= MAX and not dist[nx]:
        dist[nx] = dist[x] + 1
        queue.append(nx)

MAX = 10 ** 5
n, k = map(int, input().split())
dist = [0] * (MAX + 1)

bfs(n, k)
