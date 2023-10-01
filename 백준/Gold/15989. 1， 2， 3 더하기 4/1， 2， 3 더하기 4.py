T = int(input())

for _ in range(T):
  n = int(input())
  d = [1] * (n+1)
  for i in range(2, n+1):
    d[i] += d[i-2] 
  for i in range(3, n+1):
    d[i] += d[i-3] 
  print(d[n])