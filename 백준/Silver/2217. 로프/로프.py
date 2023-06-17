n = int(input())
ropes = []
max_value = 0

for _ in range(n):
  ropes.append(int(input()))

ropes.sort()
for i in range(n):
  tmp = ropes[i] * (n-i)
  max_value = max(max_value, tmp)

print(max_value)