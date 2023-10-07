import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
  max_value = 0
  min_value = float('inf')

  w = input().strip()
  k = int(input())
  count = defaultdict(list)
  for i in range(len(w)):
    if w.count(w[i]) >= k:
      count[w[i]].append(i)
  for arr in count.values():
    for j in range(len(arr)-k+1):
      tmp = arr[j+k-1] - arr[j] + 1
      min_value = min(min_value, tmp)
      max_value = max(max_value, tmp)

  if min_value == float('inf') and max_value == 0:
    print(-1)
  else:
    print(min_value, max_value)