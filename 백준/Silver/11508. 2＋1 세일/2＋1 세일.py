n = int(input())
prices = []
res = 0

for _ in range(n):
  prices.append(int(input()))

prices.sort(reverse=True)

i = 0
while i + 2 < n:
  res += prices[i] + prices[i+1]
  i += 3

while i < n:
  res += prices[i]
  i += 1

print(res)