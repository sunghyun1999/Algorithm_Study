t = int(input())

for i in range(t):
  data = input()
  balance = 0
  for i in range(len(data)):
    if balance < 0:
      break
    if data[i] == '(':
      balance += 1
    elif data[i] == ')':
      balance -= 1
  
  if balance == 0:
    print('YES')
  else:
    print('NO')