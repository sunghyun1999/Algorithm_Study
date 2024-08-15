x, y = 0, 0
max_value = 0
for i in range(9):
  data = list(map(int, input().split()))
  for j in range(len(data)):
    if data[j] == max(data) and data[j] >= max_value:
      max_value = data[j]
      x = i + 1
      y = j + 1

print(max_value)
print(x, y)