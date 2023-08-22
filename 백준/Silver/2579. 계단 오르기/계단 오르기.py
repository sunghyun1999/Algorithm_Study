n = int(input())

d = [0] * (n+1)
stairs = [int(input()) for _ in range(n)]

d[1] = stairs[0]
if n >= 2:
  d[2] = stairs[0] + stairs[1]
for i in range(3, n+1):
  d[i] = max(d[i-2] + stairs[i-1], d[i-3] + stairs[i-2] + stairs[i-1])

print(d[n])