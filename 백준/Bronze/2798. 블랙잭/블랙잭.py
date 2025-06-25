from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
for combi in combinations(data, 3):
    total = sum(combi)
    if total <= m:
        answer = max(answer, total)

print(answer)
