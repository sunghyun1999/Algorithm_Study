from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

result = 0
for case in permutations(data, n):
  tmp = 0
  for i in range(n-1):
    tmp += abs(case[i]-case[i+1])
  result = max(result, tmp)

print(result)