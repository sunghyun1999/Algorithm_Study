n = int(input())

border_len = 4 * n - 3
arr = [[' '] * border_len for _ in range(border_len)]
x, y = 0, 0

def star(num, x, y):
  if num == 1:
    arr[x][y] = '*'
    return
  for i in range(x, x+num):
    for j in range(y, y+num):
      if i == x or j == y or i == x+num-1 or j == y+num-1:
        arr[i][j] = '*'
  num -= 4
  x += 2
  y += 2
  star(num, x, y)

star(border_len, x, y)
for i in range(border_len):
  for j in range(border_len):
    print(arr[i][j], end='')
  print()