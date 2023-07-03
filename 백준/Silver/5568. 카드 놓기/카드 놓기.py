from itertools import permutations

n = int(input())
k = int(input())

arr = []
for _ in range(n):
  arr.append(input())

res = 0
data = []
for tup in permutations(arr, k):
  tmp = ''.join(tup)
  if tmp in data:
    continue
  data.append(tmp)
  res += 1

print(res)