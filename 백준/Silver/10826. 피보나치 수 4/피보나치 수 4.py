d = [0] * 10001
d[1] = 1
d[2] = 1

n = int(input())
for i in range(3, n+1):
  d[i] = d[i-2] + d[i-1]

print(d[n])