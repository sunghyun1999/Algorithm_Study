n, k = map(int, input().split())
coin_types = []
count = 0

for _ in range(n):
  coin_types.append(int(input()))

coin_types.reverse()
for coin in coin_types:
  count += k // coin
  k %= coin

print(count)