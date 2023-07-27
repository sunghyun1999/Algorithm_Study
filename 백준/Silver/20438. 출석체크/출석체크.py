import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = list(map(int, input().split()))
code = list(map(int, input().split()))
attend = [False] * (n+3)

code_sub_sleep = [c for c in code if c not in sleep]
for i in code_sub_sleep:
  for j in range(i, n+3, i):
    if j not in sleep:
      attend[j] = True

prefix_sum = [0] * (n+3)
for i in range(3, n+3):
  if not attend[i]:
    prefix_sum[i] = prefix_sum[i-1] + 1
  else:
    prefix_sum[i] = prefix_sum[i-1]

for _ in range(m):
  s, e = map(int, input().split())
  print(prefix_sum[e] - prefix_sum[s-1])