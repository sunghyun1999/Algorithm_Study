n = int(input())
answer = [0] * (n)

data = list(map(int, input().split()))
for i in range(n):
  cnt = 0
  for j in range(n):
    if answer[j] == 0 and cnt == data[i]:
      answer[j] = i + 1
      break
    elif answer[j] == 0:
      cnt += 1

for num in answer:
  print(num, end=' ')