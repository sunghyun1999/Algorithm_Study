from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')
people = [i for i in range(n)]

for team in combinations(people, n // 2):
    start_team = list(team)
    link_team = list(set(people) - set(start_team))

    start_score = sum(s[i][j] + s[j][i] for i, j in combinations(start_team, 2))
    link_score = sum(s[i][j] + s[j][i] for i, j in combinations(link_team, 2))

    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)
