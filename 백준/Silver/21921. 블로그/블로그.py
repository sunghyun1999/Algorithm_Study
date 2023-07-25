import sys 
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

interval_sum = sum(visitors[:x])
max_value = interval_sum
count = 1

for i in range(x, n):
  interval_sum += visitors[i]
  interval_sum -= visitors[i-x]
  if interval_sum > max_value:
    max_value = interval_sum
    count = 1
  elif interval_sum == max_value:
    count += 1

if max_value == 0:
  print("SAD")
else:
  print(max_value)
  print(count)