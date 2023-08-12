money = int(input())
stock = list(map(int, input().split()))

def junhyun(money, stock):
  num = 0
  for i in range(len(stock)):
    num += money // stock[i]
    money -= money // stock[i] * stock[i]
  return num * stock[len(stock)-1] + money

def sungmin(money, stock):
  rise_day = 0
  fall_day = 0
  num = 0
  for i in range(1, len(stock)):
    if stock[i] > stock[i-1]:
      rise_day += 1
      fall_day = 0
    elif stock[i] < stock[i-1]:
      fall_day += 1
      rise_day = 0
    if rise_day >= 3:
      money += stock[i] * num
      num = 0
    elif fall_day >= 3:
      num += money // stock[i]
      money -= money // stock[i] * stock[i]
  return num * stock[len(stock)-1] + money
      
if junhyun(money, stock) > sungmin(money, stock):
  print("BNP")
elif junhyun(money, stock) < sungmin(money, stock):
  print("TIMING")
else:
  print("SAMESAME")