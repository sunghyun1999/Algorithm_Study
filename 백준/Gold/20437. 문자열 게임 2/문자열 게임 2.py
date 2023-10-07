import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  max_value = 0
  min_value = 10001
  w = input().strip()
  k = int(input())
  for i in range(len(w)):
    if w[i:].count(w[i]) >= k:
      arr = []
      for j in range(i, len(w)):
        if w[j] == w[i]:
          arr.append(j)
          if len(arr) == k:
            break
      max_value = max(max_value, arr[-1]-arr[0]+1)
      min_value = min(min_value, arr[-1]-arr[0]+1)
  if max_value == 0 and min_value == 10001:
    print(-1)
  else:
    print(min_value, max_value)