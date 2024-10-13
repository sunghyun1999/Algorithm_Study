import sys
from collections import deque

input = sys.stdin.readline

def bfs():
  queue = deque([(1, 0)])
  visited = [False] * 101
  visited[1] = True

  while queue:
    now, cnt = queue.popleft()
    if now == 100:
      return cnt
    
    for i in range(1, 7):
      next_pos = now + i
      if next_pos <= 100:
        if ladder[next_pos]:
          next_pos = ladder[next_pos][0]
        elif snake[next_pos]:
          next_pos = snake[next_pos][0]
      
        if not visited[next_pos]:
          visited[next_pos] = True
          queue.append((next_pos, cnt+1))

n, m = map(int, input().split())
ladder = [[] for _ in range(101)]
snake = [[] for _ in range(101)]

for _ in range(n):
  x, y = map(int, input().split())
  ladder[x].append(y)

for _ in range(m):
  u, v = map(int, input().split())
  snake[u].append(v)

print(bfs())