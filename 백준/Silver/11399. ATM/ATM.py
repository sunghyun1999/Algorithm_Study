n = int(input())
p = list(map(int, input().split()))
res = 0
time = 0

p.sort()
for i in range(n):
  time += p[i]
  res += time

print(res)