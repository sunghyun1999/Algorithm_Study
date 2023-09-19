T = int(input())

for _ in range(T):
  n, k, t, m = map(int, input().split())
  score = [[0] * (k+1) for _ in range(n+1)]
  cnt = [0] * (n+1) 
  last_time = [0] * (n+1)
  for log in range(m):
    i, j, s = map(int, input().split())
    score[i][j] = max(score[i][j], s)
    cnt[i] += 1
    last_time[i] = log

  total = [sum(score[team]) for team in range(1, n+1)]
  result = [(team, total[team-1], cnt[team], last_time[team]) for team in range(1, n+1)]
  result.sort(key=lambda x: (-x[1], x[2], x[3]))
  for idx in range(len(result)):
    if result[idx][0] == t:
      print(idx+1)