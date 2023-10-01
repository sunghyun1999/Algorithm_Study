import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d+1)]
road = []
for _ in range(n):
  departure, arrival, distance = map(int, input().split())
  road.append((departure, arrival, distance))

road.sort(key=lambda x: (x[0], x[1]))

for i in range(len(road)):
  if road[i][1] > d:
    continue
  cnt = 0
  for j in range(road[i][1], d+1):
    dp[j] = min(dp[road[i][0]] + road[i][2] + cnt, dp[j])
    cnt += 1

print(dp[d])