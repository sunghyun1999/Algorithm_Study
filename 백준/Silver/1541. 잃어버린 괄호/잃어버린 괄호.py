arr = list(input().split('-'))

res = sum(map(int, arr[0].split('+')))
for i in range(1, len(arr)):
  val = list(map(int, arr[i].split('+')))
  res -= sum(val)

print(res)