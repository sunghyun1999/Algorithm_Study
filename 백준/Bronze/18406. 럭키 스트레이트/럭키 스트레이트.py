n = list(map(int, input()))
sum1 = sum(n[0:len(n)//2])
sum2 = sum(n[len(n)//2:])

if (sum1 == sum2):
  print("LUCKY")
else:
  print("READY")