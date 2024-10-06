from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

def bfs(start):
  check = False
  queue = deque([(start, 0)])
  visited[start] = True
  while queue:
    now, cnt = queue.popleft()
    if now == G:
      print(cnt)
      check = True
      break
    if now + U <= F and not visited[now + U]:
      queue.append((now + U, cnt + 1))
      visited[now + U] = True
    if now - D >= 1 and not visited[now - D]:
      queue.append((now - D, cnt + 1))
      visited[now - D] = True

  if not check:
    print("use the stairs")

bfs(S)
