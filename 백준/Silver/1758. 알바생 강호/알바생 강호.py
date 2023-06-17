n = int(input())
tips = []
res = 0

for _ in range(n):
  tips.append(int(input()))

tips.sort(reverse=True)
for i in range(1, n+1):
  tip = tips[i-1] - (i-1)
  if tip < 0:
    break
  res += tip

print(res)