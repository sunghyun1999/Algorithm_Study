h, num = map(int, input().split())

res = 0
for i in range(h + 1):
  hour = '0' + str(i) if i < 10 else str(i)
  for j in range(60):
    min = '0' + str(j) if j < 10 else str(j)
    for k in range(60):
      sec = '0' + str(k) if k < 10 else str(k)
      if str(num) in str(hour) + str(min) + str(sec):
        res += 1

print(res)
