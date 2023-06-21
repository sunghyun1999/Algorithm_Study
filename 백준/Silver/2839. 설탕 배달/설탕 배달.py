n = int(input())
array = [3, 5]
d = [10000] * (n+1)
d[0] = 0

for i in array:
  for j in range(i, n+1):
    if d[j-i] != 10000:
      d[j] = min(d[j], d[j-i]+1)

if d[n] == 10000:
  print(-1)
else:
  print(d[n])