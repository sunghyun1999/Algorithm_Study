import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  stock = list(map(int, input().split()))
  answer = 0
  max_value = 0
  for i in range(len(stock)-1, -1, -1):
    if stock[i] > max_value:
      max_value = stock[i]
    else:
      answer += max_value - stock[i]
  print(answer)