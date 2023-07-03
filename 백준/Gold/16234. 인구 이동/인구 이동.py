from collections import deque

n, l, r = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

def process(x, y, index):
  united = []
  united.append((x, y))

  queue = deque()
  queue.append((x, y))

  union[x][y] = index
  count = 1
  sum = data[x][y]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
        if l <= abs(data[x][y] - data[nx][ny]) and abs(data[x][y] - data[nx][ny]) <= r:
          queue.append((nx, ny))
          count += 1
          union[nx][ny] = index
          sum += data[nx][ny]
          united.append((nx, ny))

  for i, j in united:
    data[i][j] = sum // count

total_count = 0

while True:
  union = [[-1] * n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:
        process(i, j, index)
        index += 1
  if index == n*n:
    break
  total_count += 1

print(total_count)