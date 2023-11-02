from itertools import combinations

n = int(input())
s = []
for _ in range(n):
  s.append(list(map(int, input().split())))

player = [i for i in range(1, n+1)]
team = list(combinations(player, n//2))

answer = 1000
for start in team:
  tmp1 = 0
  for i in combinations(start, 2):
    tmp1 += s[i[0]-1][i[1]-1] + s[i[1]-1][i[0]-1]
  tmp2 = 0
  link = set(player) - set(start)
  for i in combinations(link, 2):
    tmp2 += s[i[0]-1][i[1]-1] + s[i[1]-1][i[0]-1]
  answer = min(answer, abs(tmp1 - tmp2))

print(answer)