import sys
input = sys.stdin.readline

num = input().strip()
idx = 0
n = 0

while True:
  n += 1
  breaker = False
  for s in str(n):
    if s == num[idx]:
      idx += 1
      if idx >= len(num):
        print(n)
        breaker = True
        break
  if breaker == True:
    break