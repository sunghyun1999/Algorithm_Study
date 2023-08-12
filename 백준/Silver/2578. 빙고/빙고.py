def check():
  cnt = 0
  for i in range(5):
    if sum(arr[i]) == 0:
      cnt += 1
  for j in range(5):
    sum_value = 0
    for i in range(5):
      sum_value += arr[i][j]
    if sum_value == 0:
      cnt += 1
  sum_value1 = 0
  sum_value2 = 0
  for i in range(5):
    sum_value1 += arr[i][i]
    sum_value2 += arr[i][5-i-1]
  if sum_value1 == 0:
    cnt += 1
  if sum_value2 == 0:
    cnt += 1
  return cnt

def bingo():
  for i in range(5):
    for j in range(5):
      num = mc[i][j]
      for k in range(5):
        for h in range(5):
          if arr[k][h] == num:
            arr[k][h] = 0
            if check() >= 3:
              print(i*5 + j + 1)
              return

arr = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
bingo()