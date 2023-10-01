import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
  sushi.append(int(input()))

for i in range(k-1):
  sushi.append(sushi[i])

event = sushi[:k]
max_len = len(set(event)) + 1 if c not in event else len(set(event))

for i in range(k, len(sushi)):
  event.pop(0)
  event.append(sushi[i])
  tmp = len(set(event)) + 1 if c not in event else len(set(event))
  if tmp > max_len:
    max_len = tmp

print(max_len)