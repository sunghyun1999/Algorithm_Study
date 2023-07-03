from itertools import product

n, k = input().split()
arr = list(input().split())
len_max = len(n)

max_num = 0
while True:
  for tup in product(arr, repeat=len_max):
    tmp = int(''.join(tup))
    if tmp <= int(n):
      max_num = max(max_num, tmp)

  if max_num != 0:
    print(max_num)
    break
  len_max -= 1