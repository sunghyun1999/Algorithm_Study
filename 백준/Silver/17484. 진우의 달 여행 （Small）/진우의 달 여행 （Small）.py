import sys

def dfs(x, y, min_value, direction):
  if x == n-1:
    global answer
    answer = min(answer, min_value)
    return
  for i in range(3):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < n and ny >= 0 and ny < m and i != direction:
      tmp = min_value + moon[nx][ny]
      dfs(nx, ny, tmp, i)

n, m = map(int, input().split())
moon = []
for _ in range(n):
  moon.append(list(map(int, input().split())))

dx = [1, 1, 1]
dy = [-1, 0, 1]

answer = int(sys.maxsize)
for i in range(m):
  dfs(0, i, moon[0][i], -1)

print(answer)