import sys
input = sys.stdin.readline

n, m = map(int, input().split())

game = []
for _ in range(n):
  title, max_power = input().split()
  game.append((title, int(max_power)))

for _ in range(m):
  power = int(input())
  start = 0
  end = n - 1
  res = 0
  while start <= end:
    mid = (start + end) // 2
    if power <= game[mid][1]:
      res = game[mid][0]
      end = mid - 1
    else:
      start = mid + 1
  print(res)