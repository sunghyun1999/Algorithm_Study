from itertools import combinations
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for case in combinations(data, 3):
  sum_value = sum(case)
  if sum_value <= m:
    result = max(result, sum_value)

print(result)