import sys
input = sys.stdin.readline

d = [0 for _ in range(100001)]
d[1] = 1
d[2] = 2
d[3] = 2
d[4] = 3
d[5] = 3
d[6] = 6
for i in range(7, 100001):
  d[i] = (d[i-6] + d[i-4] + d[i-2]) % 1000000009

T = int(input())
for _ in range(T):
  n = int(input())
  print(d[n])