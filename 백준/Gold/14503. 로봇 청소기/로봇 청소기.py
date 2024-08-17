import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
clean = [[0] * m for _ in range(n)]
clean[r][c] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

room = []
for _ in range(n):
  room.append(list(map(int, input().split())))

res = 1
nr, nc = r, c
while True:
  cnt = 0
  for _ in range(4):
    turn_left()
    cnt += 1
    nr = r + dx[d]
    nc = c + dy[d]
    if room[nr][nc] == 0 and clean[nr][nc] == 0:
      clean[nr][nc] = 1
      res += 1
      cnt = 0
      r, c = nr, nc
      break
  if cnt == 4:
    nr, nc = r - dx[d], c - dy[d]
    if room[nr][nc] == 0:
      r, c = nr, nc
    else:
      break

print(res)