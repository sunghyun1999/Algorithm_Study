n = int(input())
target = int(input())
arr = [[0] * n for _ in range(n)]
x, y = 0, 0

def snail(num, x, y):
  if num == 1:
    arr[x][y] = 1
    return
  curr = num * num
  for i in range(x, x+num-1):
    arr[i][y] = curr
    curr -= 1
  for j in range(y, y+num-1):
    arr[x+num-1][j] = curr
    curr -= 1
  for i in range(x+num-1, x, -1):
    arr[i][y+num-1] = curr
    curr -= 1
  for j in range(y+num-1, y, -1):
    arr[x][j] = curr
    curr -= 1
  snail(num-2, x+1, y+1)

snail(n, x, y)
for i in range(n):
  for j in range(n):
    if arr[i][j] == target:
      result_x, result_y = i+1, j+1
    print(arr[i][j], end=' ')
  print()
print(result_x, result_y)