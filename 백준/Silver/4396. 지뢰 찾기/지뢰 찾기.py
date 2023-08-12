n = int(input())
mine = [list(input()) for _ in range(n)]
curr = [list(input()) for _ in range(n)]

def mine_num(x, y):
  cnt = 0
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 1, -1, 0, 1]
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if mine[nx][ny] == '*':
        cnt += 1
  return cnt

def bomb():
  for i in range(n):
    for j in range(n):
      if mine[i][j] == '*':
        curr[i][j] = '*'

for i in range(n):
  for j in range(n):
    if curr[i][j] == 'x':
      if mine[i][j] == '*':
        bomb()
      else:
        curr[i][j] = mine_num(i, j)

for i in range(n):
  for j in range(n):
    print(curr[i][j], end='')
  print()