n = int(input())
arr = [-1] * (11)
result = 0

for _ in range(n):
  n, m = map(int, input().split())
  if arr[n] == -1:
    arr[n] = m
  elif arr[n] != m:
    result += 1
    arr[n] = m

print(result)