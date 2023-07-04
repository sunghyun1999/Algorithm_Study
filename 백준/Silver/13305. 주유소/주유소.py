import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = 0
curr = cost[0]
for i in range(n-1):
  if cost[i] < curr:
    curr = cost[i]
  res += curr * distance[i]

print(res)