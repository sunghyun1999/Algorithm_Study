import math
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)
d[0] = 0
d[1] = 1

for i in range(2, n+1):
  min_value = 50001
  for j in range(1, int(math.sqrt(i))+1):
    min_value = min(min_value, d[i-j**2])
  d[i] = min_value + 1

print(d[n])